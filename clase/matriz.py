sub = 0
aux = []
matriz = []
numero = int(input("¿De que tamaño desea la matriz?:"))

for n in range(numero):
	aux.append(1)
		
for n in range(numero):
	matriz.append(aux)
	
for i in matriz:
	print (i)	

print ("Diagonal de la matriz")
	
for m in matriz:
	print (m[sub])
	sub = sub + 1

print ("La matriz leida al reves") 

for i in matriz[::-1]:
	for j in i[::-1]:
		print (j)	
