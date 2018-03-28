# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: forms
# Author: mbegma
# Create data: 01.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=256)])
    submit = SubmitField('Сохранить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username')


class PostForm(FlaskForm):
    post = TextAreaField('Скажите', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Сказать')
