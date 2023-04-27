# -*- coding: UTF-8 -*-
"""
@Project ：test_fastapi 
@File    ：test.py
@Author  ：Yuqi.W
@Date    ：2022/9/16 10:55 AM 
@DOC     :
"""
from flask import Flask

app = False(__name__)

@app.route("/")
def hello_world():
    return "Hello,world!"
