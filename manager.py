from flask.ext.script import Manager

from szufm.app import app


application = app('szufm', 'development.conf')
application.debug = True


manager = Manager(application)


if __name__ == '__main__':
    manager.run()
