def router2(app):
    @app.route('/')
    def hello_world() -> str:
        return 'Hello World!'
