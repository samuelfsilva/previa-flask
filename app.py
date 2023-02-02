from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/criar_swi")
def criar_swi():
    return render_template("criar_swi.html")

@app.route("/novo_dcp")
def novo_dcp():
    return render_template("novo_dcp.html")

@app.route("/continuar_dcp")
def continuar_dcp():
    return render_template("continuar_dcp.html")

if __name__ == "__main__":
    app.run(debug=True)
