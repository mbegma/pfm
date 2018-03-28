# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: pfm
# Name: __init__.py
# Author: mbegma
# Create data: 28.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
