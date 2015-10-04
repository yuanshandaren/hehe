#encoding=utf-8
from . import app
from flask import render_template,flash,redirect,url_for,request
from model import Post,Tag
from form import EditPostForm

@app.route('/')
def index():
    page = request.args.get('page',1,type=int)
    pagination = Post.query.order_by(Post.create_time.desc()).paginate(
        page,per_page=4,error_out=False)
    posts = pagination.items
    return render_template('index.html',posts=posts,p=pagination)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('post.html',post=post)

@app.route('/tag/<int:tag_id>')
def show_tag(tag_id):
    tag = Tag.query.filter_by(id=tag_id).first()
    post = tag.posts
    pagination = post.order_by(Post.create_time.desc()).paginate(
        1,per_page=4,error_out=False)
    posts = pagination.items
    return render_template('show_tag.html',posts=posts,p=pagination,tag=tag.name)

@app.route('/comment')
def comment():
    return render_template('show_comment.html')










