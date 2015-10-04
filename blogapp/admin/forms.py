#encoding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from blogapp.model import User
from wtforms import validators
#from werkzeug.security import check_password_hash
class LoginForm(Form):
    name = StringField('name',validators=[Required()])
    password  = StringField('password')

    def get_user(self):            #得到用户
        user = User.query.filter_by(name=self.name.data).first()
        return user

    def validate_name(self, field):  #检查密码正确
        user = self.get_user()
        if user:
            if user.password != self.password.data:
                raise validators.ValidationError('password error')
        else:
            raise validators.ValidationError('user error')


