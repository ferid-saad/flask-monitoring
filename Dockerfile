
# 1. Image Python de base
FROM python:3.10-slim

# 2. Définir le répertoire de travail
WORKDIR /app

# 3. Copier le code source
COPY app.py .

# 4. Installer les dépendances
RUN pip install --no-cache-dir flask prometheus-client

# 5. Exposer le port de l'application
EXPOSE 5000

# 6. Démarrer l'application Flask
CMD ["python", "app.py"]
