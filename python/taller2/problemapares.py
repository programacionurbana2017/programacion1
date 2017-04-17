numero = "1,2,5,4,3,6,7,8,9"

contador = 0
print (numero)
for i in numero:
	if i == ",":
		i = ""
	else:
		if int(i)%2 == 0:
			contador = contador + 1
			print ((i)+(" es un numero par"))
	
	
print (("En la cadena de texto hay "),(contador),(" Numeros pares"))
	
