from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

neighList = {
    "neighborhood1",
    "neighborhood2",
    "neighborhood3"
}

@app.route("/")
def show_home_neighScore():
    return render_template("neighScore.html", topNeighList = neighList)

