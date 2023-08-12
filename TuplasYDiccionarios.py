# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mails.txt"
handle = open(name)

# Se separa la parte que necesito del texto
conteo = {}
for oraciones in handle:
    if oraciones.startswith('From '):
        oracion = oraciones.split()
        segmento = oracion[5]
        separacion = segmento.strip().split(':')[0]
# Se hace un conteo de valores iguales, en caso de que no exista será igual a 1, si no se suma.
        conteo[separacion] = conteo.get(separacion, 0) + 1

# Se trasnforma el diccionario en una tupla y luego se añade a una lista vacia quedando valores (key,value) ó (x,y) para poder sortear la lista y luego imprimir value, key
lista = []
for key, value in conteo.items():
    tupla = (key, value)
    lista.append(tupla)
    orden = lista.sort()

for value, key in lista:
    print(value, key)





# OUTPUT:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1







