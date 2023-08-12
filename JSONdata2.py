import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Esta API require de una KEY para acceder
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Se solicita una Locacion
direccion = input('Elija una direccion ')
# URL de partida
initialURL = 'http://py4e-data.dr-chuck.net/json?'

# Se arma un diccionario para poder codificar el input de la locación (en las URLS se reflejan como pares EJ: address=?xyxyxy -- EJ2: Universidad de Venezuela → address=Universidad+de+Venezuela&key=42, ver Print(parseInput))
inputParams = dict()
inputParams['address'] = direccion
# Se añade al diccionario otro dato, (dato key=value) → api_key = ((key = 42))
if api_key is not False: inputParams['key'] = api_key

# Se parsea el input URL completo quedando el initialURL + el input parseado
parseInput = urllib.parse.urlencode(inputParams)
finalURL = initialURL + parseInput
# print(finalURL)
# print(parseInput)

# Se abre la URL con un handle
whand = urllib.request.urlopen(finalURL)
# Se decodifica la resputa para poder trabajar lo que necesite
info = whand.read().decode()
# print(info)

# Se analiza la cadena de texto en formato JSON y se convertierte en un objeto de Python (diccionario) para despues poder pedirle la info a extraer.
js = json.loads(info)
# print(js)

# Se solicita la información a extraer
placeID = js['results'][0]['place_id']
print(placeID)

# FINISH
# OUTPUT : ChIJky9zq9BYKowRQJOcyaRjBFU (Universidad de Venezuela)












