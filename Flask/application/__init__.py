from flask import render_template, url_for
import json
import plotly
import plotly.express as px
from flaskext.markdown import Markdown
from flask import Flask

app = Flask(__name__)
Markdown(app)

@app.route("/")
def index():
    mkd_text = "## Your Markdown Here "
    return render_template("index.html",mkd_text=mkd_text)


@app.route('/charts')
def chart1():
    # Graph One
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)
    graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

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
