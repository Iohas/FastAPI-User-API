API de Usuários com FastAPI e Docker
Uma API RESTful simples para gerenciar informações de usuários, conteinerizada para fácil implantação.

Sumário
✨ Visão Geral

🚀 Primeiros Passos

Pré-requisitos

Clonar o Repositório

Iniciar a Aplicação

Acessar a API

🧪 Uso da API

Criar um Usuário (POST /users/)

Consultar um Usuário (GET /users/{user_id})

📁 Estrutura do Projeto

🤝 Contribuição

📄 Licença

✨ Visão Geral
Este projeto implementa uma API RESTful simples utilizando FastAPI em Python para o gerenciamento de informações de usuários. As funcionalidades incluem a consulta e a adição de registros de usuários, com persistência de dados em um banco de dados SQLite. A aplicação é completamente conteinerizada e orquestrada com Docker, garantindo um ambiente de desenvolvimento e implantação consistente e portátil.

🚀 Primeiros Passos
Siga as instruções abaixo para configurar e iniciar a API em sua máquina local.

Pré-requisitos
Certifique-se de ter o Docker Desktop (que inclui o Docker Engine e o Docker Compose) instalado e em execução em seu sistema operacional.

1. Clonar o Repositório
Comece clonando o projeto para sua máquina local e navegando até o diretório raiz do projeto:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

2. Iniciar a Aplicação com Docker Compose
Dentro do diretório raiz do projeto (onde o arquivo docker-compose.yml está localizado), execute o seguinte comando no terminal:

docker compose up --build -d

Este comando orquestrará o ambiente da API:

Construirá a imagem Docker da sua API com base no Dockerfile.

Criará e iniciará um contêiner Docker para sua API.

Configurará a persistência do banco de dados SQLite, mapeando-o para a pasta local ./data.

3. Acessar a API
Com o contêiner em execução, sua API estará disponível para interação. Você pode acessá-la através do seu navegador ou de ferramentas como Postman/Insomnia:

Documentação Interativa (Swagger UI):
http://localhost:8000/docs

Endpoint de Consulta (GET):
http://localhost:8000/users/{user_id}

Endpoint de Criação (POST):
http://localhost:8000/users/

🧪 Uso da API
Esta seção detalha como interagir com os endpoints da API.

Criar um Usuário (POST /users/)
Utilize este endpoint para adicionar um novo usuário ao banco de dados.

Endpoint: POST http://localhost:8000/users/

Request Body (JSON):

{
  "name": "Nome do Usuário",
  "birthday": "AAAA-MM-DD",
  "city": "Cidade do Usuário"
}

Exemplo de Resposta (200 OK):

{
  "id": 1,
  "name": "Nome do Usuário",
  "age": 30,
  "city": "Cidade do Usuário"
}

Consultar um Usuário (GET /users/{user_id})
Utilize este endpoint para obter os detalhes de um usuário existente pelo seu ID.

Endpoint: GET http://localhost:8000/users/{user_id}

Exemplo de URL: http://localhost:8000/users/1

Exemplo de Resposta (200 OK):

{
  "id": 1,
  "name": "Nome do Usuário",
  "age": 30,
  "city": "Cidade do Usuário"
}

Exemplo de Resposta (404 Not Found):

{
  "detail": "Usuário não encontrado"
}

📁 Estrutura do Projeto
Abaixo está a organização dos arquivos e diretórios do projeto:

.
├── main.py               # Lógica principal da API FastAPI.
├── requirements.txt      # Lista de dependências Python do projeto.
├── Dockerfile            # Instruções para a construção da imagem Docker da API.
├── docker-compose.yml    # Definição e orquestração dos serviços Docker.
├── .gitignore            # Regras para o Git ignorar arquivos e pastas.
├── README.md             # Este documento de visão geral do projeto.
├── data/                 # Diretório para persistência do banco de dados SQLite (gerado pelo Docker).
│   └── sql_app.db        # Arquivo do banco de dados SQLite.
└── tests/                # Diretório reservado para testes unitários e de integração.

🤝 Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar bugs, por favor, abra uma Issue ou um Pull Request.