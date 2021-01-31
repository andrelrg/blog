from flask import Flask
from routes import routes
from flask_assets import Environment


def create_app():

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()

    with app.app_context():
        from assets import compile_static_assets

        compile_static_assets(assets)


    routes(app)
    return app


app = create_app()
# route(app)


if __name__ == "__main__":
    app.run()

