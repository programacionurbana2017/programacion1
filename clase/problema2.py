numero = int(input("ingrese su numero:"))
aux = ""
aux1 = 0
aux2 = 1

for i in range(0,numero,1,):
	aux = aux + "a" 
	if i == aux1:
		for j in range(0,aux2,1,):
			aux = aux + "b"
			
	aux1 = aux1 + 1	
	aux2 = aux2 + 1
	
print (aux)