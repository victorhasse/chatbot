<div align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/AIML-PyAIML3-FF6B6B?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Online-00C851?style=for-the-badge"/>

# 🎮 SigmaBOT

**PT** | [EN](#english-version)

> Assistente virtual para compra de jogos digitais, desenvolvido com Python e AIML.

</div>

---

## 📌 Sobre o Projeto

O **SigmaBOT** é um chatbot desenvolvido para simular o atendimento virtual de uma loja de jogos digitais — a **SigmaStore**. O bot guia o usuário pelo fluxo completo de compra, desde o login até o pagamento, além de oferecer suporte para reembolsos e contato com atendentes.

Projeto desenvolvido para fins acadêmicos e de portfólio, utilizando a linguagem **AIML** como base de conhecimento e **Python** para integração com o Telegram.

---

## 🤖 Funcionalidades

- ✅ Verificação de login e cadastro
- 🛒 Lista de jogos disponíveis
- 🧺 Gerenciamento de carrinho
- 💳 Fluxo de pagamento (Pix e Cartão)
- 🔄 Solicitação de reembolso
- 📞 Contato com atendente humano
- 🔙 Opção de voltar ao menu principal a qualquer momento

---

## 🗺️ Fluxograma do Bot
```
OLA
 │
 ├── 1. Comprar Produto
 │    │
 │    ├── Logado? SIM ──► Menu Comprar
 │    │                    ├── JOGOS ──► Escolher Jogo ──► Carrinho
 │    │                    │                                  ├── PIX/CARTAO ──► PAGO ✅
 │    │                    │                                  └── REMOVER
 │    │                    └── CARRINHO
 │    │
 │    └── Logado? NAO ──► Instrução de login/cadastro
 │
 └── 2. Ajuda
      ├── REEMBOLSO ──► Informar jogo ──► Confirmar ──► Sucesso ✅
      └── ATENDENTE ──► Telefone de contato
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3.10+ | Linguagem principal |
| PyAIML3 | Motor de interpretação AIML |
| AIML | Base de conhecimento do bot |
| python-telegram-bot | Integração com Telegram |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Railway | Hospedagem em nuvem |

---

## 📁 Estrutura do Projeto
```
sigmabot/
├── venv/                  # Ambiente virtual (não versionado)
├── .env                   # Token do Telegram (não versionado)
├── .gitignore
├── brain.xml              # Base de conhecimento AIML
├── main.py                # Bot via terminal (CLI)
├── telegram_bot.py        # Integração com Telegram
├── requirements.txt       # Dependências do projeto
├── Procfile               # Configuração Railway
└── README.md
```

---

## 📸 Demonstração

> _Adicionar depois screenshots do bot funcionando no Telegram!_
> _(Tirar prints do fluxo completo de compra e do menu de ajuda)_

---

## 👤 Créditos

Desenvolvido por **Victor Hasse** e **Bernardo Santos Vieira**

[![GitHub](https://img.shields.io/badge/victorhasse-181717?style=flat&logo=github)](https://github.com/victorhasse)
[![GitHub](https://img.shields.io/badge/BernardoSVieira-181717?style=flat&logo=github)](https://github.com/BernardoSVieira)

> ⚠️ Este é um projeto pessoal desenvolvido para fins de portfólio acadêmico. Não representa uma loja real.

---

<div align="center" id="english-version">

# 🎮 SigmaBOT — English Version

> Virtual assistant for digital game purchases, built with Python and AIML.

## 📌 About

**SigmaBOT** is a chatbot that simulates a virtual store assistant for **SigmaStore**, a digital game shop. It guides users through the full purchase flow — from login to payment — and also handles refund requests and customer support redirection.

Built as an academic and portfolio project using **AIML** as the knowledge base and **Python** for Telegram integration.

## 🤖 Features

- ✅ Login and registration verification
- 🛒 Available games listing
- 🧺 Shopping cart management
- 💳 Payment flow (Pix and Credit Card)
- 🔄 Refund requests
- 📞 Human attendant contact
- 🔙 Return to main menu at any time

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python 3.10+ | Main language |
| PyAIML3 | AIML interpreter engine |
| AIML | Bot knowledge base |
| python-telegram-bot | Telegram integration |
| python-dotenv | Environment variable management |
| Railway | Cloud hosting |

## 👤 Credits

Developed by **Victor Hasse** & **Bernardo Santos Vieira**

[![GitHub](https://img.shields.io/badge/victorhasse-181717?style=flat&logo=github)](https://github.com/victorhasse)
[![GitHub](https://img.shields.io/badge/BernardoSVieira-181717?style=flat&logo=github)](https://github.com/BernardoSVieira)

> ⚠️ This is a personal project for academic portfolio purposes. It does not represent a real store.

</div>
