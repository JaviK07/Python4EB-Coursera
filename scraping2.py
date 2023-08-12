import urllib.request
from bs4 import BeautifulSoup

url = 'https://py4e-data.dr-chuck.net/known_by_Halina.html'
count = 7  # Número de veces que se debe repetir el proceso
position = 18  # Posición relativa al primer nombre

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup('a')
    url = anchors[position - 1].get('href')
    name = anchors[position - 1].text # .text extrae el texto dentro de la etiqueta (es tipo método)

print("Último nombre en la secuencia:", name)
