from flask import Flask, request, render_template, redirect
from utilities import inputQB, get_qb_id, get_player_names

app = Flask(__name__)

@app.route("/")
def index():
    player_names = get_player_names()
    return render_template("hello.html", player_names=player_names)

@app.route('/signup', methods = ['POST', "GET"])
def signup():
    if request.method == "GET":
        player_names = get_player_names()
        return render_template("hello.html", player_names=player_names)

    qb_id = get_qb_id(request.form['firstname'])
    return redirect("/stats/" + qb_id)

@app.route("/stats/<playerID>", methods = ["GET"])
def stats(playerID):
    return str(inputQB(playerID, "yards")) + "<br>" + str(inputQB(playerID, "TD"))


#if you go to /tombrady/tds you should get the results

if __name__ == '__main__':
    app.run(debug = True)
