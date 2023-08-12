import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


fhand = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1797166.xml')
data = fhand.read().decode() # Lee y decodifica los datos en formato texto
tree = ET.fromstring(data) # Crea el objeto ElementTree a partir de la cadena de texto
# ↑ A partir de acá ya se puede trabajar con lo que está dentro del XML

desglose = tree.findall('comments/comment')

count = 0
for item in desglose:
    recoleccion = int(item.find('count').text)
    count = count + recoleccion
print(count)



























