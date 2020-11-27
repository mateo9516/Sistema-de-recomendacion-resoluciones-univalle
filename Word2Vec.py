import os
import sys 
import json
import nltk
from gensim.models import Word2Vec
from nltk.tokenize.toktok import ToktokTokenizer
import nltk.data
import csv
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

#Este se ejecuta de quuinto



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
model = Word2Vec(all_words, size=200, window = 10, min_count=5, workers=3) # este es el modelo del word2vec

#vocabulario = word2vec.wv.vocab

# busco palabras similares, solo se puede con palabras que esten en el vocabulario
# es decir aun no hay contexto :(                                                        
sim_words = model.wv.most_similar('reingreso',topn=30) 

print(sim_words)  # imprimo las palabras similares, en nuestra prueba solo le atino a una, 
# la palabra "negra" 

##with tempfile.NamedTemporaryFile(prefix='gensim-model-', delete=False) as tmp:
    ##temporary_filepath = tmp.name
    ##model.save(temporary_filepath)


##print(temporary_filepath)

##### de aqui pa abajo mapeo######

#model = gensim.models.Word2Vec.load(temporary_filepath)

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

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 30)
    for i in selected_indices:
        plt.annotate(labels[i], (x_vals[i], y_vals[i]))

    plt.show()    

print("al try")


#try:
 #   print("en el try")
  #  get_ipython()
#except Exception:
 #   print("Jejeje")
  #  plot_function = plot_with_matplotlib
#else:
 #   print("Jajaja")
 #   plot_function = plot_with_plotly

#plot_with_plotly(x_vals, y_vals, labels)
plot_with_matplotlib(x_vals, y_vals, labels)
#plot_function = plot_with_plotly
#plot_function(x_vals, y_vals, labels)