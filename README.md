<h1 align="center">🐶 OlaDog! Petshop AI</h1>

<p align="center">
  <strong>Assistente Virtual de Atendimento com IA Generativa, LLaMA 3.1 & Streamlit</strong>
</p>

<p align="center">
  Desenvolvido para atender tutores em tempo real, respondendo dúvidas sobre serviços, agendamentos e produtos com base exclusivamente na documentação oficial do petshop.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Groq-API-orange" alt="Groq API">
  <img src="https://img.shields.io/badge/LLaMA-3.1%208B%20Instant-purple" alt="LLaMA 3.1">
  <img src="https://img.shields.io/badge/UX%20Design-Conversational-green" alt="UX Conversacional">
</p>

---

## 📖 Sobre o Projeto

O **OlaDog!** é um assistente virtual inteligente (personificado pelo mascote **Toddy**) projetado para otimizar e humanizar o atendimento de um petshop.

A aplicação utiliza **Full Context Injection** em conjunto com o modelo **LLaMA 3.1 (8B Instant)** via **Groq Cloud API**, permitindo que o agente responda sobre agendamentos, precificação por porte, serviço de TaxiDog e produtos da lojinha com total precisão.

Antes de enviar qualquer resposta, o sistema consulta a base de manuais operacionais e aplica **Guardrails de UX e Segurança**, garantindo:
- Respostas **empáticas** e **sem alucinações**;
- Citação automática das **fontes** consultadas no rodapé;
- Protocolo imediato de **orientação de emergência** em casos de cães doentes/prostrados.


---
## 🚀 Como Funciona

O fluxo da aplicação foi desenhado para ser leve, fluido e de baixíssima latência:

1. O tutor envia uma dúvida pela interface do chat.
2. O sistema carrega os manuais operacionais (`.md`) e os combina com o **System Prompt de UX**.
3. O histórico recente de conversas é anexado para manter a memória imediata do contexto.
4. O modelo **LLaMA 3.1 8B** processa a solicitação via **Groq API**.
5. O Toddy responde de forma conversacional e insere a citação dos manuais consultados no rodapé.

---

## ✨ Funcionalidades

- 💬 Chat interativo em tempo real com avatar personalizado do Toddy
- 🧠 Respostas orientadas aos **manuais operacionais** (sem alucinações)
- 📌 Citação automática das **fontes** dos manuais no rodapé de cada mensagem
- 🚨 **Guardrail de segurança** para identificação de urgências veterinárias
- 🎨 Interface amigável com barra lateral informativa (Sidebar)
- 🔒 Proteção da API Key através de arquivo `.env` e `.gitignore`
- 📝 Histórico de conversa fluido com memória de curto prazo
- 📱 Design responsivo para desktop e dispositivos móveis

---

## 🎯 Principais Recursos de UX

- **Regra da Pergunta Única:** O agente faz apenas 1 pergunta por vez ao tutor, mantendo o tom fluido do WhatsApp.
- **Identificação de Porte Automática:** Mapeia peso (ex: cão de 8kg) para porte correto (Pequeno) e precificação equivalente.
- **Transparência:** O tutor sempre sabe de qual documento veio a informação prestada.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python 3.12+ | Linguagem principal |
| Streamlit | Interface Web e gerenciamento de estado |
| Groq Cloud API | Processamento de altíssima velocidade para LLMs |
| LLaMA 3.1 (8B Instant) | Modelo de linguagem e raciocínio |
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
                Groq API (LLaMA 3.1 8B)
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
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```
---
## ⚙️ Como Executar Localmente

**1. Clone o repositório**

```Bash
git clone https://github.com/seu-usuario/oladog-bot.git
```

**2. Entre na pasta do projeto**

```Bash
cd oladog-bot
```

**3. Crie e ative o ambiente virtual**

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

**4. Instale as dependências**

```Bash
pip install -r requirements.txt
```

**5. Configure a chave da API do Groq**

Crie um arquivo chamado .env na raiz do projeto (use o .env.example como guia) e insira sua chave:

```Snippet de código
GROQ_API_KEY=SUA_CHAVE_DA_GROQ_AQUI
```


**6. Execute a aplicação Streamlit**

```Bash
streamlit run main.py
```


---

## 💬 Exemplos de Respostas do Agente

**Pergunta:** 

Olá! Quanto custa o banho para o meu Dachshund de 8kg? Vocês buscam em casa?

---

**Resposta:** 

Olá! Para o seu Dachshund de 8kg, o porte é considerado Pequeno (P). O banho com tosa completa fica R$ 95,00. 🐶✂️

Sim, nós temos o serviço de TaxiDog! A taxa é de R$ 15,00 para até 5 km e R$ 25,00 para distâncias entre 5 km e 10 km. É só solicitar com 24h de antecedência.

Qual seria o melhor dia para agendarmos o banho do seu cãozinho? 🐾

Fonte(s): 01_servicos_e_politicas.md, 02_precos_e_vacinas.md


---

## 🔒 Segurança e Boas Práticas

A chave da API do Groq não é armazenada no repositório. 

Em ambiente local, as credenciais são isoladas no arquivo .env que está listado no .gitignore. 

Em produção (como no Streamlit Community Cloud), utilize o recurso Secrets para proteger a API Key.

---
## 👩‍💻 Autora
### Silvia Zattoni

---
## 📄 Licença
Este projeto foi desenvolvido para fins educacionais e de portfólio, demonstrando a integração prática de habilidades de Inteligência Artificial, Retrieval-Augmented Generation (RAG), Python, LangChain e Streamlit.

---
⭐ Apoie o projeto deixando sua estrelinha.

Desenvolvido por **Silvia Zattoni**.
