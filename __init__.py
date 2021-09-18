#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/9/18 17:43
# @Author   :Chen Shuai
# @File     :__init__.py

import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# SQLite URI compatible
WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"

app = Flask(__name__)




