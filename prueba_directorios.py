import os
import sys

entries = os.scandir('/Users/Mateo/Documents/OCR/resoluciones')
#print(entries) 

for entry in entries:
    print(entry.name)
    print(" lo proceso ....")
    outfile = entry.name
    nombre = outfile.replace("pdf","txt")
    f = open('/Users/Mateo/Documents/OCR/corpus/'+nombre,"a")
    f.write("papiii!!!")
    print(" procesado y añadido al corpus")
    os.remove(entry)
    f.close

