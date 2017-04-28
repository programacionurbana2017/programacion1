class Generador:
	def titulo(self,titulo,parrafo):
		titulo = "<h1>" + titulo + "</h1>"
		parrafo = "<p>" + parrafo + "</p>"
		return titulo+parrafo
			
	def Lista(self,lista):
		codigo = ""
		for i in lista:
			codigo = codigo + "<li>" +i+ "</li>"		
		codigo = "<ol>" + codigo + "</ol>"
		return  codigo
		
	def Tabla(self,tabla):
		codigo = ""
		
		for i in tabla:
				
				codigo = codigo + "<td>" + i.split(" ,") +  "</td>"
			
		codigo = "<table"+"<tr>"+codigo + "</tr>"+"</table>"
		return codigo

miGenerador = Generador()



archivo = open("nombres.txt", "r")





print  (miGenerador.Tabla(archivo)) 

