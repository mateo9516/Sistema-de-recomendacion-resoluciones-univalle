import json
import os
import csv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
#este se ejecuta de cuarto
#########################################################################

#########################################################################
#Enlace con el servicio
authenticator = IAMAuthenticator('gcZmVQqg0TlzEh03qurbQAYxqE-rxgJ52K3j6HowVGX-')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)
#########################################################################


#########################################################################
#Consumo el servicio
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/aa50adf8-dedb-45a1-b858-c4ac497ecb8c')
########################################################################

#########################################################################
#Saco los nombres de las resoluciones y el numero
row_count = 0  
ejemplo_dir = '/Users/Mateo/Documents/OCR/corpus/'
with os.scandir(ejemplo_dir) as ficheros:
    for fichero in ficheros:
        row_count = row_count + 1
#########################################################################

#########################################################################
#Abro txt
Archivo = open('Categorias.txt','w')
#########################################################################

#########################################################################
#Escaneo de las resoluciones
ejemplo_dir = '/Users/Mateo/Documents/OCR/corpus/'
with os.scandir(ejemplo_dir) as ficheros:
    for fichero in ficheros:
        with open('./corpus/'+fichero.name) as f:
#########################################################################


#########################################################################+
#Uso de IBM
            texto = f.read()
            response = natural_language_understanding.analyze(
            text=texto,
            features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=30)),
            language='es').get_result()
#########################################################################
            
#########################################################################
#Concateno palabras con relavancia mayor a 0.5
            PalabrasC = ""
            for keyw in response['keywords']:
                if keyw['relevance'] >= 0.5:
                    PalabrasC += keyw['text'] + ','
#########################################################################

#########################################################################
#Escribo en el txt el nombre de la resolucion con su categoria
            Archivo.write(fichero.name + '*' + PalabrasC +'\n')
#########################################################################

#########################################################################
#Guardo los archivos Json de cada resolucion           
            out_file = open('./jsons/res'+fichero.name+'.json', "w")
            json.dump(response, out_file, indent=2)
            out_file.close() 
#########################################################################

#########################################################################
#Cierro el txt
Archivo.close()
#########################################################################