# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



name = "mails.txt"
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

conteo = dict()

for mails in handle:
    if mails.startswith('From '):
        mails = mails.split()
        print(mails)
        mail = mails[1]
        conteo[mail] = conteo.get(mail, 0) + 1        
print(conteo)

highestValue = max(conteo.values())

#  el método get() debe ir sin paréntesis en el argumento key de la función max(). 
#  La razón es que get es un método de diccionario y se pasa como referencia en este caso, en lugar de llamarlo con paréntesis.
# Cuando se utiliza key=conteo.get (sin paréntesis), se está pasando el método get del diccionario conteo como una función de clave personalizada a la función max().
# La función max() utilizará esa función de clave para obtener un valor de comparación para cada elemento del diccionario antes de realizar la comparación y encontrar el máximo.

# The get() method returns the value of the item with the specified key!!!.

highestMember = max(conteo, key=conteo.get)

print(highestMember, highestValue)





# OUTPUT:
# cwen@iupui.edu 5







