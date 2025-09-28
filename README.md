# MailFlow AI - Backend 🇧🇷

## Visão Geral do Projeto:

O **MailFlow AI** é um sistema projetado para classificar e responder automaticamente e-mails, oferecendo uma solução prática para automação de comunicação.  
Este repositório contém o **backend** da aplicação, desenvolvido em **FastAPI**, que é responsável por receber requisições da interface web, processar os dados dos e-mails (texto ou arquivo) e retornar a classificação junto com uma resposta sugerida.

O frontend do projeto pode ser acessado [aqui](https://github.com/miguel-willians/mailflow).

## Tecnologias Utilizadas:

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=flat-square&logo=uvicorn&logoColor=white)
![CORS Middleware](https://img.shields.io/badge/CORS%20Middleware-FF6F00?style=flat-square&logo=fastapi&logoColor=white)

### Funcionalidades Principais:

1. **Receber e-mails em texto**

   - Endpoint dedicado para processar texto enviado via formulário.
   - Retorna a classificação e a resposta sugerida.

2. **Receber e-mails em arquivo**

   - Upload de arquivos `.txt` ou `.pdf` contendo o conteúdo do e-mail.
   - O backend realiza a leitura e processa o texto para análise.

3. **Integração com o modelo de IA**

   - O conteúdo do e-mail é enviado para um módulo que classifica e gera uma resposta sugerida automaticamente.

---

# MailFlow AI - Backend 🇺🇸

## Project Overview:

**MailFlow AI** is a system designed to automatically classify and respond to emails, providing a practical solution for communication automation.  
This repository contains the **backend** of the application, developed with **FastAPI**, which is responsible for handling requests from the web interface, processing email data (text or file), and returning the classification along with a suggested response.

The frontend of the project can be accessed [here](https://github.com/miguel-willians/mailflow).

## Technologies Used:

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)  
![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=flat-square&logo=uvicorn&logoColor=white)  
![CORS Middleware](https://img.shields.io/badge/CORS%20Middleware-FF6F00?style=flat-square&logo=fastapi&logoColor=white)

### Key Features:

1. **Receive emails as text**

   - Dedicated endpoint to process text sent via form.
   - Returns the classification and the suggested response.

2. **Receive emails as files**

   - Upload `.txt` or `.pdf` files containing the email content.
   - The backend reads and processes the text for analysis.

3. **AI Model Integration**

   - The email content is sent to a module that automatically classifies it and generates a suggested response.
