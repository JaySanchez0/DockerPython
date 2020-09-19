from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/note")
def notes():
    return jsonify({"Hola":"Mundo"})

app.run(port=80,host="0.0.0.0")