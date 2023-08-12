import re

with open('Regularexpressions.txt') as handle:
    contenido = handle.read()


y = re.findall('[0-9]+', contenido)

contador = 0
for numeros in y:
    transformacion = int(numeros)
    contador = contador + transformacion 
print(contador)


