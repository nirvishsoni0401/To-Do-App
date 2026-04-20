import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Create database object globally
mongo = PyMongo()

def creatApp():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'super-secret-key'
    
    # Get Mongo URI from environment, fallback to localhost
    # Using localhost to prevent immediate DNS crashes if .env is missing/dummy
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/todo_app")
    
    # If the user has left the dummy cluster0 address, let's fall back to localhost for at least starting the server locally.
    if "cluster0.mongodb.net" in mongo_uri and "<username>" in mongo_uri:
        print("Warning: Dummy MongoDB Atlas URI detected. Falling back to localhost:27017. Please update your .env file.")
        mongo_uri = "mongodb://localhost:27017/todo_app"
    
    app.config["MONGO_URI"] = mongo_uri
    
    # Setup MongoDB Client
    mongo.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app