# Dockerfile
FROM python:3.8-slim  

WORKDIR /app  # Set the working directory inside the container

COPY . /app 

RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies

CMD ["python", "app.py"]  # Command to run your application
