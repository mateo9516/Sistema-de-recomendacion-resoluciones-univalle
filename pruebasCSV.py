import sys
import os
import csv
import re

entries = os.scandir('/Users/Mateo/Documents/OCR/corpus')

#datos = [["nombre","texto"]]

wr = open('/Users/Mateo/Documents/OCR/prueba.txt',"w", encoding='utf-8') 

texto=""
"""
with open('/Users/Mateo/Documents/OCR/pruebas3.csv', 'a') as csvfile:
        fieldnames = ['nombre', 'texto']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:

            textoName = entry.name

            f = open('/Users/Mateo/Documents/OCR/corpus/'+textoName,'r')

            for x in f:
                if(len(x)>1):
                    texto+=x
            

            texto = texto.replace("\n"," ")
            #texto =f.read()
            texto = texto.replace(",","")
            texto = texto.replace(".","")

            print(len(texto))
    
            writer.writerows([{'nombre': textoName.replace("txt",""), 'texto': texto,}])
            texto=""
            print("writing complete") """

for entry in entries:
     textoName = entry.name
     f = open('/Users/Mateo/Documents/OCR/corpus/'+textoName,'r')
     for x in f:
        if(len(x)>1):
            texto+=x
            

     texto = texto.replace("\n"," ")
     #texto =f.read()
     texto = texto.replace(",","")
     texto = texto.replace(".","")
     #texto = texto.replace("ó","o")
     #texto = texto.replace("á","a")
     #texto = texto.replace("é","e")
     #texto = texto.replace("í","i")
     textoName= textoName.replace(".txt","")

     print(len(texto))
     escritura = textoName+", "+texto+"\n"
     wr.write(escritura)
     texto=""
     print("writing complete")

wr.close()



