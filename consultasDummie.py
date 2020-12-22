import sys
import os
import csv
import re
import json
import nltk
import numpy as np
from gensim.models import Word2Vec
from gensim.models import FastText
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import sent_tokenize
import nltk.data
from nltk.corpus import stopwords
import tempfile
from gensim.similarities.index import AnnoyIndexer

from sklearn.decomposition import IncrementalPCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import random
import plotly.offline as py
import plotly.graph_objs as go
from IPython import get_ipython

model = Word2Vec.load("word2vec.model")
#print(len(model.wv.vocab))

model.build_vocab([["beneficios","admision","afro"]], update=True)

model.train([["beneficios","admision","afro"]],total_examples=1,epochs=1)

#print(len(model.wv.vocab))

#annoy_index = AnnoyIndexer(model,100)



print('Ingrese su consulta : ')
consulta = input()
entrada = []
consulta = consulta.split()


for x in consulta:
    if x in model.wv.vocab:
        entrada.append(x)

top = model.wv.most_similar(entrada,topn=30)

lista_terminos = []
#print(top)

for palabra, valor in top:
    lista_terminos.append(palabra)

#print(lista_terminos)

matriz = []
with open('./Categorias.txt', 'rt') as f:
    lineas = f.readlines()
    for linea in lineas:
        linea = linea.split('*')
        matriz.append(linea)

aux=[]
resoluciones = []

for i in lista_terminos:
    for a,b in matriz:
        aux=re.split(' |, ',b)
        if i in aux:
            elemento = matriz.index([a,b])
            resoluciones.append(elemento)



print('puede consultar las resoluciones: ')
for i in range(len(resoluciones)):
    print(matriz[resoluciones[i]][0])
