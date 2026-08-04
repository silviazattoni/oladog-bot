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
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ Chave GROQ_API_KEY não encontrada no arquivo .env!")
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

# 4. BARRA LATERAL (SIDEBAR) - UX & Informações do Petshop
with st.sidebar:
    st.title("🐶 OláDog!")
    st.subheader("Seu pet em boas mãos 🐾")
    
    st.markdown("---")
    
    st.markdown("### ℹ️")
    st.write(
        "Estou aqui para tirar dúvidas, ajudar com agendamentos e dar as melhores sugestões para o seu cãozinho com base em nossos manuais oficiais."
    )
    
    st.markdown("---")
    
    st.markdown("### 💡 Posso te ajudar com:")
    st.markdown("""
    * ✂️ **Banho e Tosa:** Preços, portes e modalidades.
    * 🩺 **Consultas e Vacinas:** Informações e agendamentos.
    * 🚗 **TaxiDog:** Regras e taxas do serviço Leva e Traz.
    * 🧸 **Lojinha de Mimos:** Brinquedos, pelúcias e petiscos.
    * 🚨 **Urgências:** Orientações sobre plantão veterinário.
    """)
    
    st.markdown("---")
    st.caption("v1.0 • Desenvolvido com LLaMA 3.1 & Streamlit")

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

    # Pega apenas as últimas 2 mensagens para não estourar o limite de tokens da Groq
    for msg in historico_mensagens[-2:]:
        mensagens_api.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Chamada para a API
    chat_completion = client_groq.chat.completions.create(
        messages=mensagens_api,
        model="llama-3.3-70b-versatile",  # Modelo atualizado e oficial
        temperature=0.3
    )
    
    return chat_completion.choices[0].message.content

# 6. Área Principal de Chat

st.title("💬 OláDog! Chat")
st.caption("Tire suas dúvidas em tempo real com o assistente virtual")

mensagem_inicial = "Olá! Eu sou o Toddy, o assistente virtual do OláDog!Petshop 🐶🐾\n\nComo posso ajudar você e o seu cãozinho hoje? (Agendamentos, vacinas ou lojinha?)"

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": mensagem_inicial}
    ]

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user", avatar="👤").write(msg["content"])
    else:
        st.chat_message("assistant", avatar="🐶").write(msg["content"])

if prompt := st.chat_input("Ex.: 'Qual é o preço do banho e tosa para um cachorro de porte médio?'"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="👤").write(prompt)

    with st.chat_message("assistant", avatar="🐶"):
        with st.spinner("Toddy está verificando... 🦴"):
            resposta_toddy = conversar_com_toddy(st.session_state["messages"])
            st.write(resposta_toddy)

    st.session_state["messages"].append({"role": "assistant", "content": resposta_toddy})