API de Usuários com FastAPI e Docker
Este projeto implementa uma API RESTful simples desenvolvida em Python com FastAPI para gerenciar informações de usuários. Ela permite consultar detalhes de usuários e adicionar novos registros. Os dados são armazenados em um banco de dados SQLite e toda a aplicação é conteinerizada e orquestrada com Docker, garantindo portabilidade e facilidade de execução.

✨ Funcionalidades
GET /users/{user_id}: Consulta os detalhes de um usuário específico utilizando seu ID.

POST /users/: Cria um novo usuário no banco de dados.

🛠️ Tecnologias Utilizadas
FastAPI: Um framework web moderno e de alta performance para a construção de APIs.

SQLAlchemy: Uma biblioteca ORM (Object-Relational Mapper) para interagir com bancos de dados relacionais.

Uvicorn: O servidor ASGI que executa a aplicação FastAPI.

SQLite: Um banco de dados leve e baseado em arquivo, ideal para desenvolvimento e testes.

Docker & Docker Compose: Ferramentas essenciais para conteinerização e orquestração de ambientes.

🚀 Como Rodar o Projeto
Siga estes passos para configurar e iniciar a API em sua máquina local.

Pré-requisitos
Certifique-se de ter o Docker Desktop (que inclui o Docker Engine e o Docker Compose) instalado em seu sistema operacional.

1. Clone o Repositório
Clone o projeto para sua máquina e navegue até o diretório raiz:

git clone https://github.com/Iohas/FastAPI-User-API.git
cd FastAPI-User-API

2. Inicie a Aplicação com Docker Compose
Dentro do diretório raiz do projeto (onde o arquivo docker-compose.yml está localizado), execute o seguinte comando no terminal:

docker compose up --build -d

Este comando irá:

Construir a imagem Docker da sua API com base no Dockerfile.

Criar e iniciar um contêiner Docker para a sua API.

Configurar a persistência do banco de dados SQLite, mapeando-o para a pasta local ./data para garantir que os dados não sejam perdidos.

3. Acesse a API
Com o contêiner em execução, sua API estará acessível:

Documentação Interativa (Swagger UI):
http://localhost:8000/docs

Endpoint de Consulta (GET):
http://localhost:8000/users/{user_id}

Endpoint de Criação (POST):
http://localhost:8000/users/

📁 Estrutura do Projeto
.
├── main.py               # Lógica principal da API FastAPI.
├── requirements.txt      # Lista de dependências Python do projeto.
├── Dockerfile            # Instruções para a construção da imagem Docker da API.
├── docker-compose.yml    # Definição e orquestração dos serviços Docker.
├── .gitignore            # Regras para o Git ignorar arquivos e pastas.
├── README.md             # Este documento de visão geral do projeto.
├── data/                 # Diretório para o banco de dados SQLite (gerado pelo Docker).
│   └── sql_app.db        # Arquivo do banco de dados SQLite.
└── tests/                # Diretório reservado para testes unitários e de integração.
