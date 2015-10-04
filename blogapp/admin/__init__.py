#encoding=utf-8
from flask.ext.admin import Admin
from views import UserView,MyIndexView,PostView,MyAdminView
from blogapp.model import User,Post,Friend_link,Tag
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin.contrib.sqla import ModelView
db = SQLAlchemy()      #db为什么可以是空的？？
def create_admin(app=None):
    admin = Admin(app,name='YuanshanAdmin',index_view=MyIndexView(),
              base_template='admin/master.html')
    admin.add_view(UserView(User,db.session))
    admin.add_view(PostView(Post,db.session))
#    admin.add_view(ModelView(Friend_link, db.session))
    admin.add_view(MyAdminView(Tag, db.session))