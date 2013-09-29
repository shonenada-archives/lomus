from flask import Flask
from flask.ext.gears import Gears
from flask.ext.sqlalchemy import SQLAlchemy

from szufm.asset import setup_compilers, setup_compressors
from szufm.database import setup_database
from szufm.views.master import master_app


gears = Gears()
db = SQLAlchemy()


def app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('szufm.settings')
    app.config.from_pyfile(config)

    gears.init_app(app)
    setup_compressors(app)
    setup_compilers(app)

    db.init_app(app)
    setup_database(app)

    app.register_blueprint(master_app)

    return app
