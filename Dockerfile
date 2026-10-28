# Define a imagem base leve do sistema
FROM python:3.11-slim

# Define a pasta central de operações dentro do contentor
WORKDIR /app

# Garante o envio imediato de logs para o terminal sem armazenamento em buffer
ENV PYTHONUNBUFFERED=1

# Copia o código fonte local para a pasta do contentor
COPY src/ /app/src/

# Comando de arranque para disparar a aplicação CLI
CMD ["python", "src/main.py"]
