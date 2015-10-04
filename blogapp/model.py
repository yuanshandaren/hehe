#encoding=utf-8
import datetime
from flask.ext.login import UserMixin
from base import db

tag_post = db.Table('tags_posts',
                db.Column('tags_id', db.Integer, db.ForeignKey('tags.id')),
                db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'))
                )
class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime(),default= datetime.datetime.now())
    modify_time = db.Column(db.DateTime(),default= datetime.datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tags = db.relationship('Tag', secondary=tag_post, backref=db.backref('posts', lazy='dynamic'))
#    tags = db.Column(db.Text,default='dd')
    status = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Post %r>' % self.title

    def __unicode__(self):
        return self.title

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))
    posts = db.relationship("Post",backref='author',lazy='dynamic')
    description =db.Column(db.Text)
    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.nickname

    def __unicode__(self):
        return self.name

# 友链
class Friend_link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    link = db.Column(db.String(120))

# 标签
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    def __repr__(self):
        return '<Tag %r>' % self.name
    def __unicode__(self):           #不加这个，显示的是<Tag u'hhh>
        return self.name



