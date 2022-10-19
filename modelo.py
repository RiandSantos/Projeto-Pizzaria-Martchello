import torch
import torch.nn as nn

class RedeNeural(nn.Module):
    def __init__(self, tamanho_entrada, tamanho_oculto, num_classes):
        super(RedeNeural, self).__init__()
        self.l1 = nn.Linear(tamanho_entrada, tamanho_oculto)
        self.l2 = nn.Linear(tamanho_oculto, tamanho_oculto)
        self.l3 = nn.Linear(tamanho_oculto, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        saida = self.l1(x)
        saida = self.relu(saida)
        saida = self.l2(saida)
        saida = self.relu(saida)
        saida = self.l3(saida)
        return saida
        
