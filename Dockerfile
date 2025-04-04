# Usa imagem oficial do Python
FROM python:3.11-slim

# Cria um diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependências primeiro
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Define a porta (caso seu app use, tipo Flask)
EXPOSE 5000

# Comando para rodar a aplicação (ajuste para seu app)
CMD ["python", "app.py"]