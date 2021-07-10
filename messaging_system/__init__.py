import logging
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from messaging_system.settings import Setting

db = SQLAlchemy()  # done here so that db is importable
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

MESSAGES_LIST_FILE_PATH = 'local_json_data/data.json'


def create_app(config_class=Setting):
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask
        from messaging_system.views.index_route import index_route
        from messaging_system.views.messages_routes import messages_router
        # Create messaging_system
        app = Flask(__name__)
        # Key
        app.config.from_object(Setting)
        app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
        # Database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        """
        Routes
        """
        messages_router(app)
        index_route(app)

        """
        Initilize DB
        """

        return app
    except Exception:
        logger.exception(f"Error starting flask App")
        raise
