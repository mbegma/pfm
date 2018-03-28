# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: microblog
# Name: models
# Author: mbegma
# Create data: 01.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


# Таблица ассоциаций подписчиков
# followers = db.Table('followers',
#                      db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
#                      db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
#                      )


# Пользователи
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    measurements = db.relationship('Measurement', backref='author', lazy='dynamic')

    about_me = db.Column(db.String(256))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # followed = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id == id),
    #     secondaryjoin=(followers.c.followed_id == id),
    #     backref=db.backref('followers', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{0}?d=identicon&s={1}'.format(digest, size)

    # def is_following(self, user):
    #     return self.followed.filter(followers.c.followed_id == user.id).count() > 0
    #
    # def follow(self, user):
    #     if not self.is_following(user):
    #         self.followed.append(user)
    #
    # def unfollow(self, user):
    #     if self.is_following(user):
    #         self.followed.remove(user)
    #
    # def followed_posts(self):
    #     followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
    #         followers.c.follower_id == self.id)
    #     own = Post.query.filter_by(user_id=self.id)
    #     return followed.union(own).order_by(Post.timestamp.desc())


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    measurement_1 = db.Column(db.Float)
    measurement_2 = db.Column(db.Float)
    measurement_3 = db.Column(db.Float)
    average_value = db.Column(db.Float)
    max_value = db.Column(db.Float)
    min_value = db.Column(db.Float)
    comment = db.Column(db.String(255))

    def __repr__(self):
        return '<Measurement {0}>'.format(self.id)

# Посты пользователей
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
