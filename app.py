from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify

from chat import get_resposta

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    texto = request.get_json().get("mensagem")
    # TODO: checar se o texto foi valido
    respostas = get_resposta(texto)
    mensagem = {"resposta": respostas}
    return jsonify(mensagem)

if __name__ == "__main__":
    app.run(debug=True)