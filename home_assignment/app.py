import logging
from controllers.index_route import index_route
from controllers.messages_routes import messages_router
from database import db

MESSAGES_LIST_FILE_PATH = 'local_json_data/data.json'


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask, request, json
        from controllers import messages_routes
        # Create app
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
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


if __name__ == '__main__':
    app = create_app()
    app.run()
