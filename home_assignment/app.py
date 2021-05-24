import os
import logging

from home_assignment.controllers.config import obj


def initialize_data(messages_list):
    result = []
    for message in messages_list:
        result.append(message)
    return result


# Connect to DataBase
data_base = initialize_data(obj)


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

        return app2
    except Exception:
        logger.exception(f"Error starting flask App")
        raise






