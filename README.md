# Containerized Flask Application with MongoDB

This project demonstrates how to build and run a containerized web application using Flask as the web framework and MongoDB as the database. The application is fully containerized using Docker, allowing easy setup and deployment across different environments.

## Key Features
- **Flask**: A lightweight web framework to create a REST API.
- **MongoDB**: A NoSQL database for storing data in a JSON-like format.
- **Docker**: Containerized setup for easy orchestration and deployment.

## How to Run
- Clone the repository.
- Build and run the Docker containers with `docker-compose up`.
- Access the Flask application via [http://localhost:5000](http://localhost:5000).

## Setup
### Create a Virtual Environment
Open a terminal and run the following commands:
```bash
python -m venv flask-env
.\flask-env\Scripts\activate
pip install flask pymongo
```

### Create a Project Structure
Open a folder called `login-page` in VSCode and create the following structure:
```
login-page/
|-- docker-compose.yml
|-- flask/
    |-- app.py
    |-- Dockerfile
    |-- requirements.txt
    |-- static/
        |-- style.css
    |-- templates/
        |-- index.html
```

### Create docker-compose.yml
Inside the `login-page` folder, create a `docker-compose.yml` file:
```yaml
version: '3.8'

services:
  mongo_db:
    image: mongo:5.0
    ports: 
      - "27018:27017"
    environment:
      MONGO_INITDB_DATABASE: user_profiles
    networks:
      - flask-mongo-network

networks:
  flask-mongo-network:
    driver: bridge
```

### Create app.py
Inside the `flask` folder, create an `app.py` file:
```python
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__) 
client = MongoClient('mongodb://mongo_db:27017/')
db = client.user_profiles
collection = db.profiles

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/thank_you')
def thank_you():
    return "<h1> Thank you! Your profile has been created successfully!</h1>"

@app.route('/submit', methods=["POST"])
def submit():
    user_data = {
        'name': request.form.get("name"),
        'email': request.form.get("email"),
        'age': request.form.get("age")
    }
    collection.insert_one(user_data)
    return redirect(url_for("thank_you"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Create Dockerfile
In the `flask` folder, create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Create requirements.txt
In the terminal, navigate to the `flask` folder and create the `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

### Create index.html
In the `templates` folder, create an `index.html` file:
```html
<!DOCTYPE html>
<head>
    <title>User Profile Creation</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Create a New User Profile</h1>
        <form action="/submit" method="POST">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            <label for="age">Age:</label><br>
            <input type="number" id="age" name="age" required><br><br>
            <button type="submit">Save Profile</button>
        </form>
    </div>
</body>
</html>
```

### Create style.css
In the `static` folder, create a `style.css` file:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    text-align: center;
}

.container {
    margin-top: 50px;
}

h1 {
    color: #333;
}

form {
    display: inline-block;
    text-align: left;
    margin: 0 auto;
}

input {
    margin-bottom: 10px;
    padding: 8px;
    width: 250px;
}

button {
    padding: 10px 15px;
    background-color: #5cb85c;
    color: white;
    border: none;
    cursor: pointer;
}
```

## Running the Application
In the terminal, navigate to the `login-page` folder and run:
```bash
docker-compose up --build
```

## Accessing the Application
Open your browser and go to [http://localhost:5000](http://localhost:5000) to see the login page. Upon submitting a profile, you should see a success message.

## Checking Data in MongoDB
To check the submitted data, access the MongoDB container:
```bash
docker exec -it mongo_db bash
```
Then, use the Mongo shell:
```bash
mongosh
show dbs
use user_profiles
show collections
db.profiles.find()
```

