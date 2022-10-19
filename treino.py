import numpy as np
import random
import json

from nltk_utilitarios import tokenizacao, derivacao, mochila_de_palavras

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from modelo import RedeNeural

with open('intencoes.json', 'r') as f:
    intencoes = json.load(f)

todas_palavras = []
acoes = []
xy = []
for intencao in intencoes['intencoes']:
    acao = intencao['acao']
    acoes.append(acao)
    for padrao in intencao['padroes']:
        p = tokenizacao(padrao)
        todas_palavras.extend(p)
        xy.append((p, acao))

palavras_ignoradas = ['?', '!', '.', ',']
todas_palavras = [derivacao(p) for p in todas_palavras if p not in palavras_ignoradas]
todas_palavras = sorted(set(todas_palavras))
acoes = sorted(set(acoes))


x_treino = []
y_treino = []
for (padrao_sentenca, acao) in xy:
    mochila = mochila_de_palavras(padrao_sentenca, todas_palavras)
    x_treino.append(mochila)

    etiqueta = acoes.index(acao)
    y_treino.append(etiqueta) 

x_treino = np.array(x_treino)
y_treino = np.array(y_treino)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_sample = len(x_treino)
        self.x_data = x_treino
        self.y_data = y_treino

    #dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_sample

batch_size = 8
tamanho_oculto = 8
saida_tamanho = len(acoes)
tamanho_entrada = len(x_treino[0])
taxa_aprendizagem = 0.001
num_periodos = 1000

dataset = ChatDataset()
treino_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

dispositivo = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
modelo = RedeNeural(tamanho_entrada, tamanho_oculto, saida_tamanho).to(dispositivo)

criterios = nn.CrossEntropyLoss()
otimizador = torch.optim.Adam(modelo.parameters(), lr=taxa_aprendizagem)

for periodo in range(num_periodos):
    for (palavras, etiquetas) in treino_loader:
        palavras.to(dispositivo)
        etiquetas = etiquetas.to(dtype=torch.long).to(dispositivo)

        saidas = modelo(palavras)
        perda = criterios(saidas, etiquetas)

        otimizador.zero_grad()
        perda.backward()
        otimizador.step()
    
    if(periodo +1) %100 == 0:
        print(f'periodo {periodo+1}/{num_periodos}, perda={perda.item():.4f}')

print(f'perda final, perda={perda.item():.4f}')

data = {
    "modelo_estado": modelo.state_dict(),
    "tamanho_entrada": tamanho_entrada,
    "saida_tamanho": saida_tamanho,
    "tamanho_oculto": tamanho_oculto,
    "todas_palavras": todas_palavras,
    "acoes": acoes
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'treino completo. arquivo salvo para {FILE}')





