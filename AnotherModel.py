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

# este se ejecuta segundo
"""
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
 # con esto separo todas las palabras de las supuestas oraciones
model = Word2Vec(all_words, size=350, window = 7, min_count=5, workers=4,sg=0) # este es el modelo del word2vec
#modelFT = FastText(all_words ,size=300, window = 8, min_count=5, workers=3)

model.save("word2vec67.model")
#modelFT.save("FastText.model")
"""
#vector = model.wv["afrocolombiano"]
model=Word2Vec.load("word2vec69.model")
#print(vector)

sim_words = model.wv.most_similar('rendimiento',topn=30)

for palabra,valor in sim_words:
    print(palabra,',',valor)
