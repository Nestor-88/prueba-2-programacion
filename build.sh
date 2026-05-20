#!/bin/bash

# Generar el Dockerfile dinámicamente
echo "Creando Dockerfile..."
cat << 'EOF' > Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY clima.py .
CMD ["python", "clima.py"]
EOF

# Construir la imagen Docker
echo "Construyendo la imagen Docker 'clima-sur-app'..."
docker build -t clima-sur-app 

# Ejecutar el contenedor pasando la variable de entorno de la MV
echo "Ejecutando el contenedor con el nombre 'samplerunning'..."
docker run --name samplerunning -e API_KEY_PROYECTO=$API_KEY_PROYECTO clima-sur-app
