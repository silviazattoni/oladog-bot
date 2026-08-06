<h1 align="center">🐶 OláDog! Petshop AI</h1>

<p align="center">
  <strong>Assistente Virtual de Atendimento com IA Generativa, LLaMA 3.3 & Streamlit</strong>
</p>

<p align="center">
  Desenvolvido para atender tutores em tempo real, respondendo dúvidas sobre serviços, agendamentos e produtos com base exclusivamente na documentação oficial do petshop.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Groq-API-orange" alt="Groq API">
  <img src="https://img.shields.io/badge/LLaMA-3.3%2070B-purple" alt="LLaMA 3.3">
  <img src="https://img.shields.io/badge/UX%20Design-Conversational-green" alt="UX Conversacional">
</p>

---

## 📖 Sobre o Projeto

O **OláDog!** é um assistente virtual inteligente (personificado pelo mascote **Toddy**) projetado para otimizar e humanizar o atendimento de um petshop.

A aplicação utiliza **Full Context Injection (RAG Estrito)** em conjunto com o modelo **LLaMA 3.3 (70B Versatile)** via **Groq Cloud API**, permitindo que o agente responda sobre agendamentos, precificação por peso/porte, serviço de TaxiDog e produtos da lojinha de forma objetiva e precisa.

Antes de enviar qualquer resposta, o sistema consulta a base de manuais operacionais e aplica **Guardrails de UX e Segurança**, garantindo:
- Respostas **empáticas**, **diretas** e **sem alucinações**;
- Citação automática das **fontes** consultadas no rodapé;
- Protocolo imediato de **orientação de emergência** em casos de cães doentes/prostrados;
- Direcionamento seguro para **Agenda Online** e **Loja Virtual fictícia**.

---

## 🚀 Como Funciona

O fluxo da aplicação foi desenhado para ser leve, fluido e de baixíssima latência:

1. O tutor envia uma dúvida pelo campo de texto ou clica em uma das **sugestões rápidas**.
2. O sistema carrega a base de conhecimento (`data/01_*.md` a `03_*.md`) e o **System Prompt com Guardrails (`04_system_prompt.md`)**.
3. O histórico recente de conversas é anexado para manter a memória de contexto.
4. O modelo **LLaMA 3.3 70B** processa a solicitação via **Groq API**.
5. O Toddy responde de forma assertiva, cordial e insere a citação dos manuais no rodapé.

---

## ✨ Funcionalidades

- 💬 Chat interativo em tempo real com avatar personalizado do Toddy (`🐶`)
- 🧹 **Botão de Limpar Conversa** na barra lateral para resetar a sessão a qualquer momento
- ⚡ **Botões de Atalho para Dúvidas Frequentes** na tela principal
- 🧠 Respostas estritamente orientadas aos **manuais operacionais** (zero alucinações)
- 📌 Citação automática das **fontes** dos manuais no rodapé de cada mensagem
- 🚨 **Guardrail de segurança** para identificação de urgências veterinárias
- 🎨 Interface amigável com barra lateral informativa (Sidebar)
- 🔒 Suporte a variáveis de ambiente (`.env` local e `st.secrets` no Streamlit Cloud)
- 📱 Design responsivo para desktop e dispositivos móveis

---

## 🎯 Principais Recursos de UX

- **Triagem de Precificação por Peso:** Exige a confirmação do peso em kg para cães antes de informar valores de banho/tosa.
- **Respostas Assertivas e sem Redundância:** Comunicação focada, sem repetir avisos não solicitados ou frases condicionais ("seria R$ X").
- **Links Úteis sem Venda Direta:** Redirecionamento amigável para agenda online e e-commerce fictício.
- **Transparência:** Citação explícita das fontes de conhecimento no final da resposta.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python 3.12+ | Linguagem principal |
| Streamlit | Interface Web e gerenciamento de estado (`session_state`) |
| Groq Cloud API | Processamento de altíssima velocidade para LLMs |
| LLaMA 3.3 (70B Versatile) | Modelo de linguagem e raciocínio avançado |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Markdown (`.md`) | Arquitetura e modularização da base de conhecimento |

---

## 🏗️ Arquitetura

```text
                     Usuário (Tutor)
                            │
                            ▼
                   Interface Streamlit
                            │
                            ▼
            System Prompt + Histórico Otimizado
                            │
                            ▼
             Base de Conhecimento (Manuais .md)
                            │
                            ▼
                Groq API (LLaMA 3.3 70B)
                            │
                            ▼
             Resposta ao Usuário + Fontes (.md)

```
---
## 📁 Estrutura do Projeto

```text
oladog-bot/
│
├── data/
│   ├── 01_servicos_e_politicas.md
│   ├── 02_precos_e_vacinas.md
│   ├── 03_loja_de_produtos.md
│   └── 04_system_prompt.md
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```
---
## ⚙️ Como Executar Localmente

**1. Clone o repositório**

```Bash
git clone [https://github.com/silviazattoni/oladog-bot.git](https://github.com/silviazattoni/oladog-bot.git)
cd oladog-bot
```

**2. Crie e ative o ambiente virtual**

**No Windows:**

```Bash
python -m venv venv
venv\Scripts\activate
```

**No Linux / macOS:**

```Bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**

```Bash
pip install -r requirements.txt
```

**4. Configure a chave da API do Groq**

Crie um arquivo .env na raiz do projeto com a sua chave:

```Snippet de código
GROQ_API_KEY=sua_chave_groq_aqui
```


**5. Execute a aplicação Streamlit**

```Bash
streamlit run main.py
```


---

## 💬 Exemplos de Respostas do Agente

**Pergunta:** 

Olá! Quanto custa o banho para o meu Dachshund de 7kg?

---

**Resposta:** 

Para o seu Dachshund de 7kg, os valores são:

• **Banho Simples:** R$ 50,00

• **Banho + Tosa Higiênica:** R$ 70,00

• **Banho + Tosa Completa:** R$ 95,00 🐶

Para agendar o melhor dia e horário para o seu cãozinho, basta acessar nossa agenda online: oladog.com.br/agendar 🐾

**Fonte(s):** 02_precos_e_vacinas.md


---

## 🔒 Segurança e Boas Práticas

A chave da API do Groq não é armazenada no repositório. 
Em ambiente local, as credenciais são isoladas no arquivo .env (ignorado via .gitignore). 
Em produção (Streamlit Community Cloud), o projeto utiliza o gerenciamento nativo via st.secrets.

---
## 👩‍💻 Autora
### Silvia Zattoni

---
## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio, demonstrando a integração prática de habilidades de Inteligência Artificial, Retrieval-Augmented Generation (RAG), Python, UX Design e Streamlit.

A aplicação é uma entrega prática do **Tech AI Builder**, a segunda fase do programa **ONE AI for Tech**, que reúne formações focadas em Inteligência Artificial e Cloud — uma iniciativa realizada pela **Oracle** em parceria com a **Alura**.

---
<div align="center">
⭐ Apoie o projeto deixando sua estrelinha.

Desenvolvido por **Silvia Zattoni**.
</div>
