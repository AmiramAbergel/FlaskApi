import logging

from home_assignment.controllers import hello_route


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask, request, json
        from home_assignment.controllers import messages_routes
        # Create app
        app = Flask(__name__)

        """
        Routes
        """
        messages_routes.router(app)
        hello_route.router2(app)

        """
        Initilize DB
        """

        return app
    except Exception:
        logger.exception(f"Error starting flask App")
        raise






