from flask import Flask

from szufm.extensions import gears, db
from szufm.extensions import setup_compilers, setup_compressors, setup_database
from szufm.master.view import master_app


def create_app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('szufm.settings')
    app.config.from_pyfile(config)

    if app.config['SENTRY_ON']:
        from raven.contrib.flask import Sentry
        sentry = Sentry(app)

    gears.init_app(app)
    setup_compressors(app)
    setup_compilers(app)

    db.init_app(app)
    setup_database(app)

    app.register_blueprint(master_app)

    return app
