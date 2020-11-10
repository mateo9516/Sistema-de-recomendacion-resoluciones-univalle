import os
import sys 
import json
import nltk
from gensim.models import Word2Vec
from nltk.tokenize.toktok import ToktokTokenizer
import nltk.data
import csv

#entries = os.scandir('./jsons') #escaneo la carpeta con los jsons
entries =  os.scandir('./corpus')

vocabulario = []

nube = ""

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle') #necesario para que separe las unidades semanticas en español

row_count = 0    
with open('./normal.csv', 'rt',encoding="utf8") as f:
    row_count = sum(1 for row in f)
    #print(row_count)

f.close()

with open('./normal.csv', 'rt',encoding="utf8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for i in range(1, row_count):
        #print(i)
        nube += mycsv[i][1]

#for entry in entries:

    #print(entry.name)
   # palabras = ""
   # f = open('/Users/Mateo/Documents/OCR/corpus/'+entry.name,'r')
   # for x in f:
   #    if(len(x)>1):
   #        palabras+=x
    
    
    #datos = open('./corpus/'+entry.name)

    #palabras = palabras.replace("\n"," ")
    #print(len(palabras['keywords']))
    #for i in range(len(palabras['keywords'])):
        #if float(palabras['keywords'][i]['relevance']) > 0.4: ## evaluo la relevancia de la palabra para agregarla a la nube
            #nube += palabras['keywords'][i]['text']+" "
    #nube += palabras+" "

all_sentences = tokenizer.tokenize(nube) # tokenize todo el texto nube, se debe hacer este paso primero sino separa por letras... Aqui saco "oraciones"
all_words = [nltk.word_tokenize(sent) for sent in all_sentences] # con esto separo todas las palabras de las supuestas oraciones
word2vec = Word2Vec(all_words, size=200, window = 10, min_count=1, workers=3) # este es el modelo del word2vec

#vocabulario = word2vec.wv.vocab

# busco palabras similares, solo se puede con palabras que esten en el vocabulario
# es decir aun no hay contexto :(                                                        
sim_words = word2vec.wv.most_similar('reingreso',topn=30) 

print(sim_words)  # imprimo las palabras similares, en nuestra prueba solo le atino a una, 
# la palabra "negra" 