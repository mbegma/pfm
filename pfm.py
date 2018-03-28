# -*- coding:utf-8 -*-
# -----------------------------------------------------
# Project Name: pfm
# Name: pfm
# Author: mbegma
# Create data: 28.03.2018
# Description: 
# Copyright: (c) Дата+, 2018
# -----------------------------------------------------
# Параметры запуска:
# set FLASK_APP=pfm.py
# set FLASK_DEBUG=1
# Запуск:
# flask run
# flask shell
# Миграция:
# flask db init - инициализация
# flask db migrate -m "new fields in user model" - создание миграции
# flask db upgrade - применение изменений миграции

from app import create_app, db
from app.models import User, Measurement

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Measurement': Measurement}
