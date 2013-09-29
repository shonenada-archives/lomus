from flask import Flask


def app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('szufm.settings')
    if not config:
        app.config.from_pyfile(config)

    return app
