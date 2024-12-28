# Utiliser une image de base officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer Poetry et les dépendances, puis installer tesseract-ocr-fra
RUN pip install poetry && \
    poetry install --no-dev && \
    apt update && \
    apt install tesseract-ocr-fra -y

# Exposer le port sur lequel l'application va tourner
EXPOSE 8501

# Commande pour lancer l'application avec Gunicorn
CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]