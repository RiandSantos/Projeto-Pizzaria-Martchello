import nltk 
import numpy as np
from nltk.stem.porter import PorterStemmer
deri = PorterStemmer()

def tokenizacao(sentenca):
    return nltk.word_tokenize(sentenca)

def derivacao(palavra):
    return deri.stem(palavra.lower())

def mochila_de_palavras(tokenizacao_sentenca, todas_palavras):
    """
    sentenca = ["Ola", "como", "voce", "vai"]
    palavras = ["Oi", "Ola", "Eu", "como", "voce", "vai", "tchau", "obrigado", "legal"]
    mala.....= [  0,    1,     0,     1,      1,     1,      0,         0,        0]
    """
    tokenizacao_sentenca = [derivacao(p) for p in tokenizacao_sentenca]

    mochila = np.zeros(len(todas_palavras), dtype=np.float32)
    for idx, p, in enumerate(todas_palavras):
        if p in tokenizacao_sentenca:
            mochila[idx] = 1.0

    return mochila


