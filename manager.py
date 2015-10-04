from blogapp import app
from base import db
from flask.ext.script import Manager
from model import Post

manager = Manager(app)

@manager.command
def save():
    post = Post(content='haha',title='d')
    db.session.add(post)
    db.session.commit()

if __name__ == '__main__':
    manager.run()