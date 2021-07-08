
def index_route(app):

    @app.route('/')
    def hello_world() -> str:
        return 'Hello World!'
