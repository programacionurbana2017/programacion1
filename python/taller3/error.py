contador = 0
numero = 2 

while (True):
    try:
        numero = numero ** numero
        contador = contador + 1
    except: 
        break

print (contador)