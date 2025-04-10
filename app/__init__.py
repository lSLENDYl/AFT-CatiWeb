from flask import Flask

app = Flask(__name__)

app.secret_key = "iyu3rg32vngt7634gv748ct834"

from app import routes

if __name__ == "__main__":
    app.run(debug=True)