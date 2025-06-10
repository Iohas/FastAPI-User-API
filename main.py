from fastapi import FastAPI, HTTPException, Depends
from datetime import date, datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# --- Configuração do Banco de Dados SQLite ---
# Nome do arquivo do banco de dados. Será criado na mesma pasta da main.py
# OU, se usar Docker Volumes, no caminho mapeado.
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/sql_app.db"

# Cria o "motor" do banco de dados SQLAlchemy.
# O connect_args é necessário para SQLite, para permitir múltiplas threads acessarem o DB.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Base para os modelos de dados que serão mapeados para as tabelas do DB.
Base = declarative_base()

# Uma SessionLocal é a classe que criará uma nova sessão de banco de dados para cada requisição.
# Cada instância de SessionLocal será uma sessão de DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Modelo de Dados (Tabela) ---
class User(Base):
    __tablename__ = "users" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthday = Column(Date) # Usamos o tipo Date do SQLAlchemy para armazenar datas
    city = Column(String)

# --- Criação das Tabelas ---
# Esta função cria as tabelas no banco de dados, se elas ainda não existirem.
def create_db_tables():
    Base.metadata.create_all(bind=engine)

# --- Funções Auxiliares de DB ---
# Função para obter uma sessão de DB e garantir que ela seja fechada após a requisição.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Instância do FastAPI ---
app = FastAPI()

# Chama a função para criar as tabelas quando a aplicação é iniciada.
@app.on_event("startup")
async def startup_event():
    create_db_tables()
    # Nenhuma adição de dados iniciais aqui! O banco de dados começará vazio.

# --- Lógica de Negócio ---
def calculate_age(birthday: date) -> int:
    """
    Calcula a idade a partir da data de nascimento.
    """
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# --- Modelos Pydantic para Requisições/Respostas ---
class UserCreate(BaseModel):
    name: str
    birthday: date
    city: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int # A idade será calculada e retornada
    city: str

    class Config:
        orm_mode = True # Habilita o modo ORM para Pydantic lidar com objetos SQLAlchemy

# --- Endpoints da API ---

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Consulta um usuário pelo ID.
    """
    user_data = db.query(User).filter(User.id == user_id).first()
    
    if not user_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    age = calculate_age(user_data.birthday)

    # Retorna os dados do usuário, incluindo a idade calculada
    return UserResponse(
        id=user_data.id,
        name=user_data.name,
        age=age,
        city=user_data.city
    )

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Cria um novo usuário no banco de dados.
    """
    db_user = User(name=user.name, birthday=user.birthday, city=user.city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Atualiza o objeto para ter o ID gerado pelo DB

    # Calcula a idade para a resposta
    age = calculate_age(db_user.birthday)
    
    return UserResponse(
        id=db_user.id,
        name=db_user.name,
        age=age,
        city=db_user.city
    )