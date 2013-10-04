from flask import Blueprint, render_template


master_app = Blueprint('master', __name__, template_folder='../templates')


@master_app.route('/')
def index():
    return render_template('index.html')


@master_app.route('/fm')
def fm():
    return render_template('fm.html')


@master_app.route('/about')
def about():
    return render_template('about.html')


@master_app.route('/join')
def join():
    return render_template('join.html')


@master_app.route('/help')
def help():
    return render_template('help.html')
