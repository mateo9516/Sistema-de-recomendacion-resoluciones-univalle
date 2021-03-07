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
"""
################# HM 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")
import pandas as pd
import numpy as np
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
    #all_sentences[i] = re.sub(r"\b[a-zA-Z]\b","",all_sentences[i])
    all_sentences[i] = re.sub(r"\W*\b\w{1,3}\b","",all_sentences[i])

#print(all_sentences)
print(len(all_sentences))

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
#all_words = [toktok.tokenize(sent) for sent in sent_tokenize(all_sentences, language='spanish')]
#rint(all_words[0])
### inicializo el modelo 
model = Word2Vec(size=350, window = 7, min_count=5, workers=4,sg=0)

model.build_vocab(all_words)
 # con esto separo todas las palabras de las supuestas oraciones
model.train(all_words, epochs=20, total_examples=model.corpus_count) # este es el modelo del word2vec
#modelFT = FastText(all_words ,size=300, window = 8, min_count=5, workers=3)


model.save("word2vecHM.model")
#modelFT.save("FastText.model")

def draw_factors_heatmap(words):
    #get words
    topwords = np.array(model.wv.index2entity)
    #get the ids of words we are interested in
    ind = np.where(np.isin(topwords, words))[0]
    #extract values from word2vec
    data = pd.DataFrame(model.wv.vectors_norm[ind, :], 
	                    index = topwords[ind],
                        columns = list(range(10)))
    #draw heatmap
    sns.heatmap(data, 
	            cmap = sns.diverging_palette(250, 10, s = 90, as_cmap = True),
                vmax = data.values.max(), vmin = data.values.min(), 
                square = True, linewidths = 2, cbar = False)
    plt.yticks(rotation = 0)
    plt.show()

#mostrando 

draw_factors_heatmap(['resolucion','academica','pregrado','regionales','matricula','derechos'])
"""

model = FastText.load("C:/Users/Mateo/Documents/OCR/modelosAutogenerados/FTCbow/FTCBoW0.model")

top = model.wv.most_similar(["calendario"],topn=30)
for i in top:
    print(i)

##vector = model.wv["afrocolombiano"]
##print(vector)


