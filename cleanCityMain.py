from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

neighList = {
    "neighborhood1" : "Pittsburgh",
    "neighborhood2" : "Philidelphia",
    "neighborhood3" : "Harrisburg",
    "neighborhood4" : "Erie"
}

personList = {
    "John" : 500,
    "Alice" : 450,
    "Emily" : 440,
    "Mike" : 400
}

#git push --set-upstream origin main
@app.route("/neighborhoodScore")
def show_neighScore():
    return render_template("neighScore.html", topNeighList = neighList)

@app.route("/home")
def show_home():
    return render_template("home.html")

@app.route("/individualCleaning")
def show_individualClean():
    return render_template("indivClean.html")

@app.route("/cleaningEvent")
def show_cleaningEvents():
    return render_template("cleaningEvent.html")

@app.route("/about")
def show_about():
      return render_template("about.html")

@app.route("/contact")
def show_contact():
      return render_template("contact.html")

@app.route("/prizes")
def show_prizes():
    return render_template("prize.html")

@app.route("/indivScore")
def show_indivScore():
    return render_template("indivScore.html", topContr = personList)

app.run()