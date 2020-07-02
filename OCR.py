from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)
import os 

#Ruta del OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta del pdf
PDF_file='/Users/Mateo/Documents/OCR/Resolucion No. 128-2020 actividades bonificables.pdf'
  
''' 
Part #1 : Convertir pdfs a imagenes
'''
# Arreglo de paginas ... convertidas a bytes
pages = convert_from_bytes(open(PDF_file,'rb').read())
#pages = convert_from_path(PDF_file,500)

# Contador para recorrer arreglo
image_counter = 1
   
for page in pages: 
  
    # cada pagina del PDF a JPG 
    # para cada pagina el nombre del archivo sera: 
    # PDF page 1 -> page_1.jpg 
    # PDF page 2 -> page_2.jpg 
    # PDF page 3 -> page_3.jpg 
    # .... 
    # PDF page n -> page_n.jpg 
    filename = "page_"+str(image_counter)+".jpg"
    print("pagina")  
    # Guardo la imagen en el sistema
    page.save(filename, 'JPEG') 
  
    image_counter = image_counter + 1
  
''' 
Parte #2 - OCR 
'''
# Variable to get count of total number of pages 
filelimit = image_counter-1
  
# Creacion del archivo plano de salida
outfile = "Resolucion2020.txt"
  
#   
# el texto de todas las imagenes es añadido al archivo plano 
f = open(outfile, "a") 
  
# ciclo para todas las paginas 
for i in range(1, filelimit + 1): 
  
    # Accedo a los archivos  
    # page_1.jpg 
    # page_2.jpg 
    # .... 
    # page_n.jpg 
    filename = "page_"+str(i)+".jpg"
          
    # usamos pytesseract para convertir la imagen a texto 
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
  
    # The recognized text is stored in variable text 
    # Any string processing may be applied on text 
    # Here, basic formatting has been done: 
    # In many PDFs, at line ending, if a word can't 
    # be written fully, a 'hyphen' is added. 
    # The rest of the word is written in the next line 
    # Eg: This is a sample text this word here GeeksF- 
    # orGeeks is half on first line, remaining on next. 
    # To remove this, we replace every '-\n' to ''. 
    text = text.replace('-\n', '')     
  
    # escribo el texto en el archivo plano 
    f.write(text) 
  
f.close() 
