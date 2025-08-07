from flask import Flask
from pymongo import MongoClient
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize MongoDB connection
    try:
        client = MongoClient(app.config['MONGODB_URI'])
        app.db = client.get_default_database()

        client.admin.command('ping')
        print("MongoDB connection successful")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        app.db = None
    
    # Routes
    @app.route('/')
    def index():
        return f"Welcome to the Shipments API!"
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.health import health_bp
    from app.routes.store import store_bp
    from app.routes.plans import plans_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(plans_bp)
    
    return app