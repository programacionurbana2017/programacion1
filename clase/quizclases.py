class Persona ():
	def __init__(self,nombre,apellido,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
	
class Estudiante(Persona):
	def __init__(self,nombre,apellido,edad,nombrecolegio,grado):
		super().__init__(nombre,apellido,edad)
		self.nombredocente = nombrecolegio
		self.grado = grado
		
class Docente(Persona):
	def __init__(self,nombre,apellido,edad,nombredocente,asignatura):
		super().__init__(nombre,apellido,edad)
		self.nombredocente = nombredocente
		self.asignatura = []
		self.asignatura.append(asignatura)
		

unestudiante = Estudiante("Gabriel","Marquez","8","Escuelita a","3")	
undocente = Docente("Gabriel","Marquez","8","Escuelita a","matematicas")

print (unestudiante.grado)
print (unestudiante.nombre)

print (undocente.nombre)
print (undocente.asignatura[0])

for i in archivo:
	print (i.split(" ,"))
		
	
