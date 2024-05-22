# Establecer la imagen base
FROM python:3.11.8

# Crear el directorio de la aplicación en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto
COPY ./app /app

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]