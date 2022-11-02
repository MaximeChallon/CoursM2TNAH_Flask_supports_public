from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/home/<string:id>")
def home(id:str):
    return "Hello world! On a demandé l'identifiant " + id