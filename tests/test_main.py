# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importa a instância 'app', 'Base', 'User' e 'get_db' do seu main.py
from main import app, Base, User, get_db

# --- IMPORTAÇÃO CORRIGIDA ---
from datetime import date, datetime # <--- Adicione datetime aqui
# ---------------------------

# --- Configuração do Banco de Dados de Teste ---
# Para testes, usaremos um banco de dados SQLite em memória
# Isso garante que cada execução de teste comece com um DB limpo e não altere o DB real.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # Usamos um arquivo para que o DB persista durante os testes

# Cria um novo motor de banco de dados para os testes
engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma sessão local de banco de dados para os testes
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# --- Fixture para o Cliente de Teste FastAPI ---
# Uma 'fixture' do pytest é uma função que é executada antes dos testes
# e pode fornecer recursos para eles.
@pytest.fixture(name="client")
def client_fixture():
    # Cria as tabelas no banco de dados de teste (limpa/recria a cada teste)
    Base.metadata.create_all(bind=engine_test)

    # Função que substitui a 'get_db' original para usar o DB de teste
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Sobrescreve a dependência de 'get_db' para usar o DB de teste
    app.dependency_overrides[get_db] = override_get_db

    # Cria o cliente de teste para a aplicação FastAPI
    with TestClient(app) as client:
        yield client # Cede o controle para os testes, mantendo o cliente ativo

    # Após os testes, exclui todas as tabelas do DB de teste
    Base.metadata.drop_all(bind=engine_test)

# --- Testes para os Endpoints da API ---

def test_create_user(client):
    # Dados do usuário a ser criado
    user_data = {
        "name": "Iohanna Test",
        "birthday": "1990-01-01",
        "city": "Test City"
    }
    # Envia uma requisição POST para o endpoint /users/
    response = client.post("/users/", json=user_data)
    
    # Verifica o status da resposta (200 OK para sucesso)
    assert response.status_code == 200
    
    # Verifica se os dados retornados estão corretos
    assert response.json()["name"] == user_data["name"]
    assert response.json()["city"] == user_data["city"]
    
    # --- Verificação de idade ajustada ---
    expected_age = datetime.now().year - int(user_data["birthday"].split('-')[0])
    assert response.json()["age"] == expected_age
    # -----------------------------------
    
    assert "id" in response.json() # Verifica se um ID foi gerado

def test_get_existing_user(client):
    # Primeiro, cria um usuário para garantir que exista um para consultar
    user_data = {
        "name": "Existing User",
        "birthday": "1985-05-10",
        "city": "Existing City"
    }
    create_response = client.post("/users/", json=user_data)
    assert create_response.status_code == 200
    user_id = create_response.json()["id"]

    # Agora, consulta o usuário pelo ID
    response = client.get(f"/users/{user_id}")
    
    # Verifica o status da resposta
    assert response.status_code == 200
    
    # Verifica os dados retornados
    assert response.json()["id"] == user_id
    assert response.json()["name"] == user_data["name"]
    assert response.json()["city"] == user_data["city"]
    
    # --- Verificação de idade ajustada ---
    expected_age = datetime.now().year - int(user_data["birthday"].split('-')[0])
    assert response.json()["age"] == expected_age
    # -----------------------------------

def test_get_non_existent_user(client):
    # Tenta consultar um ID que certamente não existe
    response = client.get("/users/99999")
    
    # Verifica se a resposta é 404 (Não Encontrado)
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"