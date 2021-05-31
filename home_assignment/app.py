import os
import logging


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask, request, json
        from home_assignment.route import config_route
        # Create app
        app2 = Flask(__name__)

        """
        Routes
        """
        config_route.router(app2)

        """
        Initilize DB
        """

        return app2
    except Exception:
        logger.exception(f"Error starting flask App")
        raise






