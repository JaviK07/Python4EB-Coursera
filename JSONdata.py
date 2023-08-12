import json
import urllib.request, urllib.error, urllib.parse

# url = JSONdata.json
url = 'https://py4e-data.dr-chuck.net/comments_1797167.json'

fhand = urllib.request.urlopen(url)
data = fhand.read().decode()
# A partir de acá ya podemos trabajar con los datos como Listas o Diccionarios según corresponda
# print(data)

info = json.loads(data)

suma = 0
for conteo in info['comments']:
    # print(conteo['count'])
    suma = suma + conteo['count']
print(suma)
