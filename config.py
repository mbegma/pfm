# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: pfm
# Name: config
# Author: mbegma
# Create data: 28.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3
