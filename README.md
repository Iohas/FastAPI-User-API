API de Usuários com FastAPI e Docker
Este projeto é uma API RESTful simples para gerenciar informações de usuários. Ela permite consultar e adicionar usuários, armazenando os dados em um banco de dados SQLite. Tudo isso é empacotado e executado facilmente com Docker.

Funcionalidades ✨
GET /users/{user_id}: Consulta os detalhes de um usuário específico pelo ID.
POST /users/: Cria um novo usuário no banco de dados.
Tecnologias Utilizadas 🛠️
FastAPI: Framework web rápido e moderno para construção de APIs.
SQLAlchemy: ORM (Object-Relational Mapper) para interação com o banco de dados.
Uvicorn: Servidor ASGI para rodar a aplicação FastAPI.
SQLite: Banco de dados leve e baseado em arquivo para persistência.
Docker & Docker Compose: Para conteinerização e orquestração da aplicação.
Como Rodar o Projeto 🚀
Siga estes passos para ter a API funcionando em sua máquina:

Pré-requisitos
Certifique-se de ter o Docker Desktop (ou Docker Engine e Docker Compose) instalado em seu sistema.

1. Clone o repositório
Bash

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
2. Inicie a aplicação com Docker Compose
Dentro do diretório raiz do projeto, execute:

Bash

docker compose up --build -d
Este comando vai:

Construir a imagem Docker da sua API.
Criar e iniciar um contêiner para a API.
Configurar a persistência do banco de dados SQLite na pasta ./data do seu projeto.
3. Acesse a API
Com o contêiner rodando, sua API estará disponível:

Documentação Interativa (Swagger UI): http://localhost:8000/docs
Endpoint de Consulta (GET): http://localhost:8000/users/{user_id}
Endpoint de Criação (POST): http://localhost:8000/users/
Estrutura do Projeto 📁
.
├── main.py               # Lógica principal da API FastAPI
├── requirements.txt      # Dependências Python
├── Dockerfile            # Instruções para a imagem Docker da API
├── docker-compose.yml    # Orquestração da aplicação com Docker Compose
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── README.md             # Documentação do projeto
├── data/                 # Pasta para o banco de dados SQLite (gerada pelo Docker)
│   └── sql_app.db        # Arquivo do banco de dados