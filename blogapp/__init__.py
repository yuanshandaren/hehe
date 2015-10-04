#encoding=utf-8
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
app = Flask(__name__)
app.config.from_object('config')

bootstrap=Bootstrap(app)
#db = SQLAlchemy(app)

app.debug = True
app.config['SECRET_KEY'] = '<replace with a secret key>'
toolbar = DebugToolbarExtension(app)

#登录配置
login_manager = LoginManager(app)
login_manager.login_view = 'login'
@login_manager.user_loader         #加载用户的回调函数
def load_user(user_id):
    from blogapp.model import User
    return User.query.filter_by(id=user_id).first()

from blogapp.admin import create_admin
create_admin(app)

import views,model
