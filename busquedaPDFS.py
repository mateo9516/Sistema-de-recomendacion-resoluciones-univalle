import sys 
import os
import shutil

entries = os.scandir('/Users/Mateo/Documents/OCR/corpus')
pdfs= os.scandir('/Users/Mateo/Documents/OCR/Teo')
f = open('/Users/Mateo/Documents/OCR/teo/noEstan.txt',"a") 
arr = []

for pdf in pdfs:
    arr.append(pdf.name)

for entry in entries:
    objetivo = entry.name
    print(objetivo)
    objetivo = objetivo.replace('txt','pdf')
    if objetivo in arr:
        shutil.copy('/Users/Mateo/Documents/OCR/Teo/'+objetivo,'/Users/Mateo/Documents/OCR/estan')
    else:
        f.write(objetivo)
        f.write('\n')
        
f.close()
 
    