# Base image will be Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# For optimization and cache usage, copy first only requirements.txt
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Then copy the rest of the files
COPY . .

# Use port 5000 for flask
EXPOSE 5000

# Run the app.py file when first running the container
CMD ["python", "app.py"]