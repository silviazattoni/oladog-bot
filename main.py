import os
import glob
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# 1. Configuração da Página do Streamlit
st.set_page_config(
    page_title="OláDog!",
    page_icon="🐶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Carrega as variáveis de ambiente
load_dotenv()

# Tenta ler do .env primeiro (local), e se não achar, busca nos secrets (Streamlit Cloud)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("❌ Chave GROQ_API_KEY não encontrada no arquivo .env nem nos Secrets!")
    st.stop()

client_groq = Groq(api_key=api_key)

# 3. Carrega o System Prompt e os Manuais (Cached)
@st.cache_data
def carregar_base_de_conhecimento():
    # Carrega System Prompt
    system_prompt_path = os.path.join("data", "04_system_prompt.md")
    with open(system_prompt_path, "r", encoding="utf-8") as f:
        system_instruction = f.read().replace("Toby", "Toddy")

    # Carrega os Manuais 01 a 03
    conhecimento = ""
    arquivos = sorted(glob.glob(os.path.join("data", "0[1-3]*.md")))
    for arq in arquivos:
        with open(arq, "r", encoding="utf-8") as f:
            nome_arquivo = os.path.basename(arq)
            conhecimento += f"\n\n=== MANIFESTO/FONTE: {nome_arquivo} ===\n" + f.read()

    return system_instruction, conhecimento

system_instruction_toddy, conhecimento_completo = carregar_base_de_conhecimento()

# Mensagem Inicial de Boas-Vindas
mensagem_inicial = "Olá! Eu sou o Toddy, o assistente virtual do OláDog!Petshop🐾\n\nComo posso ajudar você e o seu cãozinho hoje?"

# 4. BARRA LATERAL (SIDEBAR) - UX & Informações do Petshop
with st.sidebar:
    st.title("🐶 OláDog!Petshop")
    st.subheader("Seu pet em boas mãos 🐾")
        
    st.markdown("---")
    
    st.markdown("### 💡 Posso te ajudar com:")
    st.markdown("""
    * 🛁 **Banho e Tosa:** valores e modalidades.
    * 🩺 **Consultas e Vacinas:** informações de agendamento.
    * 🚗 **TaxiDog:** regras e taxas do serviço Leva e Traz.
    * 🧸 **Lojinha de Mimos:** brinquedos, pelúcias e petiscos.
    """)
    
    st.markdown("---")

    # --- BOTÃO DE LIMPAR CONVERSA ---
    if st.button("🗑️ Limpar Conversa", use_container_width=True):
        st.session_state["messages"] = [
            {"role": "assistant", "content": mensagem_inicial}
        ]
        st.rerun()

    st.caption("v1.0 • Desenvolvido com LLaMA 3.3 & Streamlit")

# 5. Função de chamada da IA com Fontes e Regras de UX
def conversar_com_toddy(historico_mensagens):
    system_prompt_ajustado = f"""
{system_instruction_toddy}

REGRAS DE CONVERSAÇÃO E UX:
1. SEJA CONVERSACIONAL E NATURAL: NUNCA responda criando formulários ou tópicos rígidos. Fale como uma pessoa no WhatsApp.
2. REGRA DA PERGUNTA ÚNICA: Faça APENAS UMA pergunta por vez para o tutor. Aguarde a resposta antes de pedir a próxima informação.
3. SEM APRESENTAÇÃO REPETIDA: Não se re-apresente ("Olá, eu sou o Toddy...") se a conversa já começou.
4. MEMÓRIA: Nunca peça informações que o tutor já deu anteriormente.

CITAGEM DE FONTES (MUITO IMPORTANTE):
No final da sua resposta, adicione sempre uma seção curta de fontes no seguinte formato (usando os nomes exatos dos arquivos consultados no contexto):

---
**Fonte(s):** [Nome do Arquivo .md]

=== BASE DE CONHECIMENTO COMPLETA OLADOG! ===
{conhecimento_completo}
"""

    # System prompt inicial com a base de conhecimento
    mensagens_api = [{"role": "system", "content": system_prompt_ajustado}]

    # Pega apenas as últimas 4 mensagens para manter contexto e economizar tokens
    for msg in historico_mensagens[-4:]:
        mensagens_api.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Chamada para a API
    chat_completion = client_groq.chat.completions.create(
        messages=mensagens_api,
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )
    
    return chat_completion.choices[0].message.content

# 6. ÁREA PRINCIPAL DE CHAT
st.title("💬 OláDog! Chat")
st.caption("Tire suas dúvidas em tempo real com o assistente virtual")

# Inicializa o histórico apenas na primeira vez
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": mensagem_inicial}
    ]

# Renderiza o histórico de mensagens
for message in st.session_state["messages"]:
    avatar_icone = "👤" if message["role"] == "user" else "🐶"
    with st.chat_message(message["role"], avatar=avatar_icone):
        st.markdown(message["content"])

# --- BOTÕES DE SUGESTÃO FIXOS ---
st.markdown("---")
st.write("✨ **Dúvidas frequentes (clique para perguntar):**")

col1, col2 = st.columns(2)
prompt_sugerido = None

with col1:
    if st.button("🐶 Quanto custa o banho simples?"):
        prompt_sugerido = "Quanto custa o banho simples para um cachorro?"
        
    if st.button("📅 Como agendar um horário?"):
        prompt_sugerido = "Como faço para agendar um atendimento?"
        
with col2:
    if st.button("💉 Quais vacinas vocês oferecem?"):
        prompt_sugerido = "Quais vacinas estão disponíveis?"
        
    if st.button("⏰ Qual o horário de funcionamento?"):
        prompt_sugerido = "Qual o horário de funcionamento do petshop?"

# --- CAMPO DE ENTRADA DO CHAT E PROCESSAMENTO ---
user_input = st.chat_input("Ex.: 'Qual é o preço do banho para um cachorro de porte médio?'")
prompt_final = prompt_sugerido or user_input

if prompt_final:
    # 1. Registra a pergunta do usuário
    st.session_state["messages"].append({"role": "user", "content": prompt_final})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt_final)

    # 2. Gera e exibe a resposta do Toddy
    with st.chat_message("assistant", avatar="🐶"):
        with st.spinner("Toddy está verificando... 🦴"):
            resposta_toddy = conversar_com_toddy(st.session_state["messages"])
            st.markdown(resposta_toddy)

    # 3. Salva a resposta no histórico e atualiza a tela
    st.session_state["messages"].append({"role": "assistant", "content": resposta_toddy})
    st.rerun()