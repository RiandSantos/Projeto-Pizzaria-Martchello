from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify
from chat import get_resposta

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.route("/cadastro") 

def cadastro():

    return render_template("cadastro.html")  

@app.route("/login") 

def login():

    return render_template("index.html")  

    
@app.route("/pedidoRestaurante")

def pedidoRestaurante():

    return render_template("PedidosRestaurante.html")

@app.route("/Sobre") 

def sobre():

    return render_template("sobreNos.html")  


@app.route("/PedidoCliente") 

def PedidoCliente():

    return render_template("PedidosCliente.html")  

@app.post("/predict")
def predict():
    texto = request.get_json().get("mensagem")
    # TODO: checar se o texto foi valido
    respostas = get_resposta(texto)
    mensagem = {"resposta": respostas}
    return jsonify(mensagem)

if __name__ == "__main__":
    app.run(debug=True)