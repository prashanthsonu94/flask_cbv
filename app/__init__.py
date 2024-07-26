from flask import Flask
from app.models import db
from app.views import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    with app.app_context():
        # Initialize the database
        db.create_all()
    
    app.register_blueprint(main_bp, url_prefix='/items')
    
    return app
