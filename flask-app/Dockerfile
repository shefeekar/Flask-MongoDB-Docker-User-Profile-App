#Build the flask appliation and its dependencies
FROM python:3.9  AS builder
WORKDIR /app
COPY requirements.txt  .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
#Buid the image from builder 
FROM python:3.9-slim
WORKDIR /app
# Copy the installed dependencies from the previous stage
COPY --from=builder /usr/local/  /usr/local/
#Copy the application source code from the previous stage
COPY --from=builder /app  /app
EXPOSE 5000
CMD ["python", "app.py"]