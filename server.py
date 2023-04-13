from flask import Flask, render_template, request, jsonify, Response
import service
from service import Service
import json
service = Service()

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/table")
def table():
    return render_template("tabulka.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/novy-hrac", methods=["POST"])
def create_player():
    data = request.json
    hrac = service.create_player(data)
    return hrac.__dict__(), 201


@app.route("/hraci", methods=['GET'])
def get_players():
    return render_template("hraci.html", hraci=service.get_all_players()), 200


@app.route("/hraci/<id>", methods=["GET"])
def get_player(id):
    hrac = service.get_player_by_id(id)
    if hrac==None:
        return "not found", 404
    return hrac.__dict__(), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

