from flask import Flask
from routes import hashers, end

def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(hashers.hashers)
        app.register_blueprint(end.endr)

    return app