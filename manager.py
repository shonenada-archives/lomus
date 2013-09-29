import os.path

from flask.ext.script import Manager

from develop_tools.clean import clean as cln
from develop_tools.pep8 import pep8
from szufm.app import app
from szufm.app import db


app_root = os.path.dirname(os.path.realpath(__name__))
conf = 'development.conf'

application = app('szufm', os.path.join(app_root, conf))
manager = Manager(application)


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
