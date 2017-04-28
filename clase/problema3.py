numero = int(input("ingrese su numero:"))
aux = ""
aux1 = 0
aux2 = 1
aux3 = numero


for i in range(0,numero,1,):
	aux = aux + "a" 
	if i == aux1:
		for j in range(0,aux2,1,):
			aux = aux + "b"
	
	if i == aux1:
		for k in range(0,aux3,1,):
			aux = aux + "c"
	
	
	aux1 = aux1 + 1	
	aux2 = aux2 + 1
	aux3 = aux3 - 1
	
print (aux)