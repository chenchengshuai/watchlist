#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2021/9/18 11:06
# @Author   :Chen Shuai
# @File     :app.py


from flask import Flask
from flask import escape, url_for


app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route("/user/<name>")
def user_page(name):
    return "user: %s" % escape(name)

@app.route("/test")
def test_url_for():
    print(url_for("hello"))

    print(url_for("user_page", name="chen"))
    print(url_for("user_page", name="wang"))

    print(url_for("test_url_for"))
    print(url_for("test_url_for", num=2))

    return "Test page"