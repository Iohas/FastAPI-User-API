# Use uma imagem base oficial do Python.
# Escolha uma versão específica que seja compatível com suas necessidades.
# 'slim-buster' é uma boa opção pois é mais leve.
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner.
# Todos os comandos subsequentes (COPY, RUN, CMD) serão executados a partir deste diretório.
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho.
# Fazemos isso primeiro para aproveitar o cache do Docker (se os requisitos não mudarem, essa etapa não é reconstruída).
COPY requirements.txt .

# Instala as dependências Python listadas no requirements.txt.
# '--no-cache-dir' é para não armazenar arquivos de cache pip, economizando espaço na imagem.
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da sua aplicação para o diretório de trabalho.
# O '.' no final significa "copiar tudo do diretório atual do host para o WORKDIR do contêiner".
COPY . .

# Expõe a porta que sua aplicação FastAPI vai usar.
# Isso apenas documenta a porta; o mapeamento real é feito no docker-compose.yml.
EXPOSE 8000

# Define o comando padrão para iniciar sua aplicação quando o contêiner é executado.
# O '--host 0.0.0.0' é crucial para que o Uvicorn ouça todas as interfaces de rede dentro do contêiner,
# tornando-o acessível de fora (via o mapeamento de portas do Docker Compose).
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
