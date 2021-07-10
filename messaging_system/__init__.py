import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # done here so that db is importable

MESSAGES_LIST_FILE_PATH = 'local_json_data/data.json'


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask, request, json, url_for
        from messaging_system.settings import Setting
        from messaging_system.views.index_route import index_route
        from messaging_system.views.messages_routes import messages_router
        # Create messaging_system
        app = Flask(__name__)
        # Key
        app.config.from_object(Setting)
        # Database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

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
