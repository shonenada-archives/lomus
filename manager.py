from flask.ext.script import Manager

from szufm.app import app
from develop_tools.clean import clean as cln
from develop_tools.pep8 import pep8


application = app('szufm', 'development.conf')
application.debug = True
manager = Manager(application)


@manager.command
def clean():
    cln


@manager.command
def check():
    pep8()


if __name__ == '__main__':
    manager.run()
