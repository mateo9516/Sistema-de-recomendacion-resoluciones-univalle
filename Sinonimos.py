import urllib, urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup as soup
import re
import json

#data = str(urllib.request.urlopen('https://educalingo.com/en/dic-es/{}'.format('contador')).read())

#final_results = re.findall('\w+', [i.text for i in soup(data, 'lxml').find_all('div', {"class":'contenido_sinonimos_antonimos0'})][0])

#print(final_results)

data = str(urllib.request.urlopen('https://www.sinonimosonline.com/correr/').read())

final_results = re.findall('\w+', [i.text for i in soup(data, 'lxml').find_all('p', {"class":'sinonimos'})][2])

print(final_results)