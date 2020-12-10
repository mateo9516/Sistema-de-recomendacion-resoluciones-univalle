import sys
import os
import csv
import re
import json
import nltk
from gensim.models import Word2Vec
from gensim.models import FastText
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import sent_tokenize
import nltk.data
from nltk.corpus import stopwords
import tempfile
##### para mapear
from sklearn.decomposition import IncrementalPCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import random
import plotly.offline as py
import plotly.graph_objs as go
from IPython import get_ipython

# este se ejecuta segundo

entries = os.scandir('/Users/Mateo/Documents/OCR/corpus')
#wr = open('/Users/Mateo/Documents/OCR/prueba.txt',"w", encoding='utf-8') 

texto=""
for entry in entries:
     textoName = entry.name
     f = open('/Users/Mateo/Documents/OCR/corpus/'+textoName,'r')
     for x in f:
        if(len(x)>1):
            texto+=x        
#wr.close()

texto = texto.replace("\n"," ")
#texto =f.read()
#texto = texto.replace(",","")
#texto = texto.replace(".","")
texto = texto.replace("ó","o")
texto = texto.replace("á","a")
texto = texto.replace("é","e")
texto = texto.replace("í","i")
texto = texto.replace("-","")
texto = texto.replace("_","")
texto = texto.replace("°","")
texto = texto.replace(")","")
texto = texto.replace("(","")
texto = texto.replace("%","")
texto = texto.replace("—","")

#Este se ejecuta de quuinto

toktok = ToktokTokenizer()

nube = texto

nltk.download('stopwords')

def normalizar_texto(texto):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;:_-]°')
    BAD_SYMBOLS_RE = re.compile('[0-9]')
    INDIVIDUAL_LETTERS = re.compile('^[a-za-z]+')
    STOPWORDS = set(stopwords.words('spanish'))
    """
        texto : string 
        
        retorna: texto modificado
    """
    texto = texto.lower()
    #texto = re.sub("[-_ ;]"," ",texto)
    texto = re.sub("[0-9]","",texto)
    texto = re.sub("\b[a-zA-Z]\b","",texto)
    aux=""
    words = texto.split()
    for r in words:
      if not r in STOPWORDS:
        aux+=r+" "
    text = aux.rstrip()
    return text

nube = normalizar_texto(nube)

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle') #necesario para que separe las unidades semanticas en español

sent = toktok.tokenize(nube)
#print(sent)
all_sentences=sent_tokenize(nube)

for i in range(len(all_sentences)):
    all_sentences[i] = re.sub("\W+"," ", all_sentences[i])
    all_sentences[i] = re.sub("\b[a-zA-Z]\b","",all_sentences[i])

#print(all_sentences)
print(len(all_sentences))

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
#all_words = [toktok.tokenize(sent) for sent in sent_tokenize(all_sentences, language='spanish')]
#rint(all_words[0])
 # con esto separo todas las palabras de las supuestas oraciones
#model = Word2Vec(all_words, size=300, window = 6, min_count=3, workers=3) # este es el modelo del word2vec
model = FastText(all_words ,size=200, window = 6, min_count=3, workers=3)

sim_words = model.wv.most_similar('afrocolombianas',topn=30) 

print(sim_words)

def reduce_dimensions(model):
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    # extract the words & their vectors, as numpy arrays
    vectors = np.asarray(model.wv.vectors)
    labels = np.asarray(model.wv.index2entity)  # fixed-width numpy strings

    # reduce using t-SNE
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


x_vals, y_vals, labels = reduce_dimensions(model)

def plot_with_plotly(x_vals, y_vals, labels, plot_in_notebook=True):
    
    trace = go.Scatter(x=x_vals, y=y_vals, mode='text', text=labels)
    data = [trace]

    if plot_in_notebook:
        py.init_notebook_mode(connected=True)
        py.iplot(data, filename='word-embedding-plot')
    else:
        print("ploteando....")
        fig = go.Figure(data=data)
        py.plot(fig)


def plot_with_matplotlib(x_vals, y_vals, labels):
   

    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)

   
    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 100)
    for i in selected_indices:
        plt.annotate(labels[i], (x_vals[i], y_vals[i]))

    plt.show()    





plot_with_matplotlib(x_vals, y_vals, labels)

