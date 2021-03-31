from flask import Flask, render_template
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

# Para correr Flask en el puerto 80 se debe correr con el comando
# authbind --deep python3 app.py
# Cualquier otro puerto por arriba de 1024 no se necesita auth
# correr directo con : 
# flask run    o    python3 app.py   o  python3 -m flask run 