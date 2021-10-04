FROM python:3.9-alpine

#Crear un directorio de trabajo que se utilizará en el contenedor
WORKDIR /app


#Variables de entorno
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

#Comandos necesarios para poder correr la aplicación
RUN apk update && apk add --no-cache gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

#Copiar los archivos al Workdir del contenedor
COPY . .

#Instalar todas las dependencias del archivo requirements
RUN pip install -r requirements.txt

#Comando para desplegar aplicación
CMD ["flask", "run"]