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
import xlsxwriter



# este se ejecuta segundo
diccionario = ["-","_","°",")","(","%","—","consejo", "academico", "universidad", "superior", "santiago de cali", "superior", "universidad","valle","resolucion","no","literal","paragrafo","reeoluciin"]
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

texto = texto.lower()
texto = texto.replace("\n"," ")
#texto =f.read()
#texto = texto.replace(",","")
#texto = texto.replace(".","")
texto = texto.replace("ó","o")
texto = texto.replace("á","a")
texto = texto.replace("é","e")
texto = texto.replace("í","i")

for d in diccionario:
    texto.replace(d,"")

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
 #### w2v #######

"""
idxModelo = 0
excel = []
for i in range(150,400,10):
    for j in range(3,11): 
        for k in range(3,30,2):
            param =[]
            param.append(idxModelo)
            param.append(i)
            param.append(j)
            param.append(k)
            model=Word2Vec(all_words, size=i, window = j, min_count=k, workers=7,sg=1)
            model.save("W2VSkipGram"+str(idxModelo)+".model")
            excel.append(param)
            idxModelo+=1


workbook = xlsxwriter.Workbook('w2vsg.xlsx')
worksheet = workbook.add_worksheet()

fila = 0 
col = 0

for idxModelo,i,j,k in excel:
    worksheet.write(fila,col,idxModelo)
    worksheet.write(fila,col+1,i)
    worksheet.write(fila,col+2,j)
    worksheet.write(fila,col+3,k)
    fila +=1

workbook.close()
"""

####### Parametros estaticos para generacion de modelos fast Text######

vec_size = [150,160,230,230,250,280,300,360]
wind = [4,6,3,4,4,4,5,3]
min_c = [7,9,5,7,7,9,9,5]

idxModelo = 0
excel = []
for i in range(len(vec_size)):
  
    param =[]
    param.append(idxModelo)
    param.append(vec_size[i])
    param.append(wind[i])
    param.append(min_c[i])
    model=FastText(all_words, size=vec_size[i], window = wind[i], min_count=min_c[i], workers=7,sg=1)
    model.save("FTSG"+str(idxModelo)+".model")
    excel.append(param)
    idxModelo+=1


workbook = xlsxwriter.Workbook('FTSG.xlsx')
worksheet = workbook.add_worksheet()

fila = 0 
col = 0

for idxModelo,i,j,k in excel:
    worksheet.write(fila,col,idxModelo)
    worksheet.write(fila,col+1,i)
    worksheet.write(fila,col+2,j)
    worksheet.write(fila,col+3,k)
    fila +=1

workbook.close()