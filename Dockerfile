# Usamos una imagen ligera de Python
FROM python:3.10-slim

# Instalamos Node.js y npm necesarios para compilar y ejecutar TypeScript
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero los archivos de dependencias de Node
COPY package*.json ./
RUN npm install

# Copiamos el resto del código del proyecto
COPY . .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Puerto predeterminado que usa Streamlit (Render suele reasignar el puerto con PORT)
EXPOSE 8501

# Comando para arrancar tu aplicación de Streamlit (app.py)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]