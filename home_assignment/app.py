import logging
from controllers.hello_route import router2
from controllers.messages_routes import router


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask, request, json
        # Create app
        app = Flask(__name__)
        """
        Routes
        """
        router(app)
        router2(app)
        """
        Initialize DB
        """
        return app
    except Exception:
        logger.exception(f"Error starting flask App")
        raise






