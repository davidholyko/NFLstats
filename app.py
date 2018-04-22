from flask import Flask, request, render_template, redirect
from utilities import inputQB

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route('/signup', methods = ['POST', "GET"])
def signup():
    if request.method == "GET":
        return render_template("hello.html")
    return redirect("/stats/" + request.form['firstname'])

@app.route("/stats/<playerID>", methods = ["GET"])
def stats(playerID):
    return str(inputQB(playerID, "yards")) + "<br>" + str(inputQB(playerID, "TD"))


#if you go to /tombrady/tds you should get the results

if __name__ == '__main__':
    app.run(debug = True)
