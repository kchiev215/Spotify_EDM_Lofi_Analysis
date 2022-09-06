from flask import render_template, url_for
import json
import plotly
import plotly.express as px
from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/charts')
def chart1():
    return render_template('charts.html')


@app.route("/introduction")
def introduction():
    return render_template("introduction.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/analysis_code")
def analysis_code():
    return render_template("analysis_code.html")
