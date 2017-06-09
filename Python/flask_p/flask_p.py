from datetime import datetime

from flask import Flask, request, current_app, make_response, abort, render_template
from flask_moment import Moment
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hhhjjjkkklll'
moment = Moment(app)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    if ('xiaoming' == name):
        abort(404)
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def before_first_request():
    print('first request')


def before_request():
    print('request before')


def after_request():
    print('request after')


def teardown_request():
    print('teardown request')


def response_h():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')


@app.route('/env')
def env():
    print(current_app.name)
    # print(app.app_context().g.__name__)
    # print(request.base_url)
    # print(session.name)
    user_agent = request.headers.get('user-agent')
    return '<p>Your browser is %s</p>' % user_agent


class NameForm(Form):
    name = StringField('What your name?', validators=[Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    manager.run()
