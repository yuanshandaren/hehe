#encoding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField
from wtforms.validators import Required, Length, Email, Regexp

class EditPostForm(Form):
    name = StringField('title',validators=[Required()])
    submit = SubmitField('update')

