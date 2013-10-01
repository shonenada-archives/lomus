import os.path

from flask.ext.script import Manager, Server

from develop_tools.clean import clean as cln
from develop_tools.pep8 import pep8
from szufm.app import create_app
from szufm.app import db


app_root = os.path.dirname(os.path.realpath(__name__))
conf = 'development.conf'

application = create_app('szufm', os.path.join(app_root, conf))
server = Server(port=5050)
manager = Manager(application)
manager.add_command("runserver", server)


@manager.command
def clean():
    cln()


@manager.command
def check():
    pep8()


@manager.command
def syncdb():
    with application.test_request_context():
        from szufm.master.model import Demo
        db.create_all()
    print 'Finished!'


if __name__ == '__main__':
    manager.run()
