from flask import Flask
# from config import Config

app = Flask(__name__)

app.secret_key = "iyu3rg32vngt7634gv748ct834"
# app.config.from_object()

from app import routes

app.run(debug=True)