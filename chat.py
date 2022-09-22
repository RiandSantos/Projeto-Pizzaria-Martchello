import random
import json
import torch
from modelo import RedeNeural
from nltk_utilitarios import mochila_de_palavras, tokenizacao

dispositivo = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intencoes.json', 'r') as f:
    intencoes = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

tamanho_entrada = data["tamanho_entrada"]
tamanho_oculto = data["tamanho_oculto"]
saida_tamanho = data["saida_tamanho"]
todas_palavras = data["todas_palavras"]
acoes = data["acoes"]
modelo_estado = data["modelo_estado"]

modelo = RedeNeural(tamanho_entrada, tamanho_oculto, saida_tamanho).to(dispositivo)
modelo.load_state_dict(modelo_estado)
modelo.eval()

nome_bot = "Arthurito"

def get_resposta(msg):
    
    sentenca = tokenizacao(msg)
    x = mochila_de_palavras(sentenca, todas_palavras)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(dispositivo)

    saida = modelo(x)
    _, predizer = torch.max(saida, dim=1)

    acao = acoes[predizer.item()]

    probabilidades = torch.softmax(saida, dim=1)
    probabilidade = probabilidades[0][predizer.item()]

    if probabilidade.item() > 0.75:
        for intencao in intencoes["intencoes"]:
            if acao == intencao["acao"]:
                return random.choice(intencao['respostas'])
    
    return "Eu não entendi"

if __name__ == "__main__":
    print("Vamos conversar! digite 'sair' para sair")
    while True:
        sentenca = input('Você: ')
        if sentenca == "sair":
            break

        resp = get_resposta(sentenca)
        print(resp)

    
    

    
