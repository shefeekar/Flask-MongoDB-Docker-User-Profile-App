#Build the flask appliation and its dependencies
FROM python:3.9  AS builder
WORKDIR /app
COPY requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#Buid the image from builder 
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app  .
EXPOSE 5000
CMD ["python", "app.py"]