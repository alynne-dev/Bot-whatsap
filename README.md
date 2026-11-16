# 🤖 Bot de Atendimento da Clínica

Bot em Python que recebe o cliente, pergunta o nome e mostra um menu de opções para agendar ou cancelar consultas.

> ⚠️ **Status:** em desenvolvimento. Por enquanto o bot roda no terminal. A integração com o WhatsApp ainda será adicionada.

## ✨ Funcionalidades

- Boas-vindas personalizadas com o nome do cliente
- Menu de opções:
  - Agendar consulta
  - Cancelar consulta

## 📋 Requisitos

- [Python 3.8+](https://www.python.org/downloads/)

## 🚀 Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/alynne-dev/whatsapp_bot.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd whatsapp_bot/Python
   ```

3. Execute o bot:

   ```bash
   python bot-whatsapp.py
   ```

## 📁 Estrutura do projeto

```
whatsapp_bot/
└── Python/
    ├── .gitignore
    └── bot-whatsapp.py
```

## 🔐 Configuração (para quando conectar ao WhatsApp)

Tokens e chaves **nunca** devem ficar no código. Crie um arquivo `.env` na pasta do projeto, seguindo o modelo abaixo:

```
WHATSAPP_TOKEN=seu_token_aqui
```

O arquivo `.env` já está no `.gitignore`, então não será enviado ao GitHub.

## 🗺️ Próximos passos

- [ ] Conectar ao WhatsApp
- [ ] Salvar os agendamentos
- [ ] Implementar o cancelamento de consultas
- [ ] Enviar lembretes de consulta

## 👩‍💻 Autora

Feito por [alynne-dev](https://github.com/alynne-dev).
