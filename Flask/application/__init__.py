import sqlite3
from turtle import title
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from dash import Dash, html

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/charts')
def chart1():
    # Graph One
    df = px.data.medals_wide()
    fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph two
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                         color='species', title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country', title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('charts.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON)


@app.route("/introduction")
def introduction():
    return render_template("introduction.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/analysis_code")
def analysis_code():
    return render_template("analysis_code.html")
