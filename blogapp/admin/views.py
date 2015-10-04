#encoding=utf-8
from flask.ext.admin import AdminIndexView,expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import login_user,current_user,logout_user
from flask import url_for,redirect
from forms import LoginForm
from wtforms import fields, widgets

class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login'))
        return super(MyIndexView, self).index()

    @expose('/login', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm()                      
        if form.validate_on_submit():
            user = form.get_user()
            login_user(user)                     #记住用户登录状态
        if current_user.is_authenticated():
            return redirect(url_for('.index'))

        self._template_args['form'] = form        #什么用？？？

        return super(MyIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))

class UserView(ModelView):
    can_create = True
    can_delete = True
    column_display_pk = True
    column_filters = ('name', 'email')               #用来设置可以筛选的栏位

#    edit_template = 'admin/edit_user.html'
#    form_overrides = dict(description=CKTextAreaField)

    form_columns = ('name', 'email', 'description')  #用于设置表单的字段，没有密码啊

    def is_accessible(self):                       #覆盖方法，只有登录才看到User界面
        return current_user.is_authenticated()


#管理post
# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):#渲染域的真正力量来自于它的 __call__() 方法. 调用(calling)域, 你可以提供关键词参数, 它们会在输出中作为HTML属性注入.
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()   #每个域(field)拥有一个Widget(部件)实例. Widget 的工作是渲染域(field)的HTML表示.

class PostView(ModelView):

    column_display_pk = True

    form_overrides = dict(content=CKTextAreaField)   #把content用ckeditor覆盖
    create_template = 'admin/create_post.html'   #将ckeditor加到模板中
    edit_template = 'admin/edit_post.html'

    column_list = ('id', 'title', 'content', 'author', 'tags', 'status', 'create_time', 'modify_time')
    # column_labels = dict(id='ID',
    #                      title=u'标题',
    #                      content=u'内容',
    #                      author=u'作者',
    #                      tags=u'标签',
    #                      status=u'状态',
    #                      create_time=u'创建时间',
    #                      modify_time=u'修改时间')

    column_choices = {
        'status': [
            (0, 'draft'),
            (1, 'published')
        ]
    }

    column_filters = ('title',)   #找题目

    column_searchable_list = ('content',)

    column_sortable_list = ('create_time', 'modify_time')

    def is_accessible(self):
        return current_user.is_authenticated()

class MyAdminView(ModelView):

    form_overrides = dict(content=CKTextAreaField)

#    create_template = 'admin/create.html'
#    edit_template = 'admin/edit.html'

    def is_accessible(self):
        return current_user.is_authenticated()

