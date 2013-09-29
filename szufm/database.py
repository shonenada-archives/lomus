def setup_database(app):
    db = app.extensions["sqlalchemy"].db

    @app.before_first_request
    def create_database_for_development():
        is_sqlite_memory =  (db.engine.url.drivername == "sqlite" and
                             db.engine.url.host in ("", ":memory:"))
        if app.config["DEBUG"] and is_sqlite_memory:
            db.create_all()
