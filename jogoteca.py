from flask import Flask

app = Flask(__name__)


@app.route("/inicio")
def ola():
    return "<h1>Ola mundo!<h1>"


app.run()
