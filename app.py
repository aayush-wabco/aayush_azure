# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:05:57 2021

@author: guptaa
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
