import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sns.set(style="white")


from gensim.models import Word2Vec, FastText

model = Word2Vec.load("C:/Users/Mateo/Documents/OCR/modelosAutogenerados/W2VSG/W2VSkipGram16.model")

model.init_sims()


#vector = model.wv.vectors_norm[0]

#print (vector)

palabras = ["afrocolombianas","equivalencias","homologacion","rendimiento","asignatura","calificacion","reingreso","exencion","matricula","cancelacion"]
#palabras = ['resolucion','academica','pregrado','regionales']

#obtengo palabras
#palabras = model.wv.index2entity[:20]
aux_fila =[]
data = []

for palabra in palabras:
    for p in palabras:
        aux_fila.append(model.similarity(p,palabra))
    data.append(aux_fila)
    aux_fila=[]


print(data)

datos= pd.DataFrame(data, index = palabras, columns = palabras)
sns.heatmap(datos,cmap = sns.diverging_palette(250, 10, s = 90, as_cmap = True),
                vmax = 1.0, vmin = 0.0, 
                square = True, cbar = False)

plt.show()

"""
topwords = np.array(model.wv.index2entity)
#obtener los indices de las palabras que me interesan 
ind = np.where(np.isin(topwords, palabras))[0]
#extract values from word2vec
data = pd.DataFrame(model.wv.vectors_norm[ind, :], index = topwords[ind], columns = list(range(150)))
#draw heatmap
sns.heatmap(data,cmap = sns.diverging_palette(250, 10, s = 90, as_cmap = True),
                vmax = data.values.max(), vmin = data.values.min(), 
                square = True, linewidths = 2, cbar = False)
plt.yticks(rotation = 0)
plt.show()
"""