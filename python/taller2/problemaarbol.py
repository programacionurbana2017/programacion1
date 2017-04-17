# Variables
a = "apkjuhybkusdobnrmsl"
b= "" 
c= ""
d= ""
g= ""
f= ""
contador = 0

# Si se encuentra la letra indicada se le asigna a la variable y se agrega una unidad al contador.
for i in a:
	if i == "a":
		b = "a"
		contador = contador+1
	if i == "r":
		c= "r"
		contador = contador+1
	if i == "b":
		d = "b"
		contador = contador+1
	if i == "o":
		g = "o"
		contador = contador+1
	if i == "l":
		f = "l"
		contador = contador+1
		
# Si el contador se supera 5 unidades signifa que si esta la palabra en caso de lo contrario no esta dicha palabra.
if contador > 4:
	print ("Verdadero la palabra arbol esta en la cadena de caracteres")
	
else: 
	print ("Falso la palabra arbol no esta en la cadena de carcateres")
		