palindromo = input("ingrese su palabra:")
p1 = ""
p2 = ""


for i in range(0,len(palindromo),1,):
	p1 = p1 + palindromo[i]
	
	
for j in range(len(palindromo)-1,-1,-1):	
			p2 = p2 + palindromo[j]
			
			
if p1 == p2:
	print ("es un palindromo")
		