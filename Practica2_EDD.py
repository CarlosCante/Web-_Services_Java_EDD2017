from flask import Flask, request, Response
app = Flask(__name__)

#Clase de la Listra Simple--------------------------------------------------------------------------------------------------------------------------------

class listaSimple():
	
	def __init__(self):
		self.Raiz = None
		self.actual = None
		self.tamano = 0
		self.grafica = "digraph Lista{"
		print("Lista Simple") 
		

	def recorrer(self, dat):
		self.grafica = "digraph Lista{"
		d = None
		aux = self.Raiz
		if aux != None:
			self.grafica = self.grafica + aux.dato
			aux = aux.siguiente

		if aux !=None:
			self.grafica = self.grafica + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente


		while aux != None:
			self.grafica = self.grafica + d + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente

		self.grafica = self.grafica + '}'
		return str(self.grafica)

	def Agregar(self, dat):
		if self.Raiz == None:
			self.Raiz = Nodo(dat, None)
			self.actual = self.Raiz
			self.tamano = self.tamano + 1
			return str(self.tamano)
		else:
			self.actual.siguiente = Nodo(dat, None)
			self.actual = self.actual.siguiente
			self.tamano = self.tamano + 1
			return str(self.tamano)

	def EliminarNodo(self, indice):
		temporal = self.Raiz

		i = 0


		if int(indice) <= self.tamano:
			while  i < int(indice):
				temporal = temporal.siguiente
				i = i + 1 


			temp2 = self.Raiz
			i=0

			while i < int(indice) - 1:
				temp2 = temp2.siguiente
				i = i + 1

			if temporal == self.Raiz:
				self.Raiz = temporal.siguiente
			else:

				if temporal == self.actual:
					temp2.siguiente = None
					self.actual = temp2
				else:
					temp2.siguiente = temporal.siguiente
			
			self.tamano = self.tamano - 1

			return str(self.tamano)
		return str(None)

			
	def BuscarNodo(self, dato):
		temporal = self.Raiz
		indice = 0
		while temporal != None:
			if temporal.dato == dato:
				return str(indice)
			indice = indice + 1
			temporal = temporal.siguiente
		return str('NO SE ENCONTRO EL DATO')


#Pila----------------------------------------------------------------------------------------------------------------------------------------------------
class Pila():
	def __init__(self):
		self.Raiz = None
		self.actual = None
		self.tamano = 0
		self.grafica = "digraph Pila{"
		print("Pila") 


	def recorrer(self, dat):
		self.grafica = "digraph Pila{"
		d = None
		aux = self.Raiz
		if aux != None:
			self.grafica = self.grafica + aux.dato
			aux = aux.siguiente

		if aux !=None:
			self.grafica = self.grafica + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente


		while aux != None:
			self.grafica = self.grafica + d + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente

		self.grafica = self.grafica + '}'
		return str(self.grafica)

	def Push(self, dato):
		if self.Raiz == None:
			self.Raiz = Nodo(dato,None)
			self.actual = self.Raiz
			self.tamano = self.tamano +1
			return str(self.tamano)
		else:
			self.actual.siguiente = Nodo(dato, None)
			self.actual = self.actual.siguiente
			self.tamano = self.tamano + 1
			return str(self.tamano)

	def Pop(self, dato):
		temporal = self.Raiz
		if temporal != None:

			if temporal.siguiente != None:
				while temporal.siguiente != None:
					if temporal.siguiente == self.actual:
						temp2 = self.actual
						temporal.siguiente = None
						self.actual = temporal
						self.tamano = self.tamano - 1
						return str(temp2.dato)
					temporal = temporal.siguiente
			else:
				temp2 = self.Raiz
				self.Raiz = None
				self.actual = self.Raiz
				self.tamano = self.tamano - 1
				return str(temp2.dato)
		else:
			return str('LA PILA ESTA VACIA')
		return str(None)

#Cola------------------------------------------------------------------------------------------------------------------------------------------------------
class Cola():
	def __init__(self):
		self.Raiz = None
		self.actual = None
		self.tamano = 0
		self.grafica = "digraph Cola{"
		print("Cola")

	def recorrer(self, dat):
		self.grafica = "digraph Cola{"
		d = None
		aux = self.Raiz
		if aux != None:
			self.grafica = self.grafica + aux.dato
			aux = aux.siguiente

		if aux !=None:
			self.grafica = self.grafica + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente


		while aux != None:
			self.grafica = self.grafica + d + '->' + aux.dato + ';' + "\n"
			d = aux.dato
			aux = aux.siguiente

		self.grafica = self.grafica + '}'
		return str(self.grafica)

	def Ingresar(self, dato):
		if self.Raiz == None:
			self.Raiz = Nodo(dato, None)
			self.actual = self.Raiz
			self.tamano = self.tamano + 1
			return str(self.tamano)
		else:
			self.actual.siguiente = Nodo(dato, None)
			self.actual =  self.actual.siguiente
			self.tamano = self.tamano + 1
			return str(self.tamano)

	def Sacar(self, dat):
		temporal = self.Raiz

		if temporal != None:	
			if temporal.siguiente == None:
				self.Raiz = None
				self.actual = None
				self.tamano = self.tamano - 1
				return str(temporal.dato)
			else:
				self.Raiz = temporal.siguiente
				self.tamano = self.tamano - 1
				return str(temporal.dato)

		return str('LA COLA ESTA VACIA')

#Matriz---------------------------------------------------------------------------------------------------------------------------------------------------
class ColumnaDominios():
	def __init__(self):
		self.Cabecera = None
		self.actual = None
		self.tamano = 0

	def AgregarNodo(self, dato):
		encontrado = False
		cadena = ''
		if self.Cabecera == None:
			for x in dato:
				if x == '@':
					econtrado = True
				if encontrado == True:
					cadena = cadena + x

			self.Cabecera = NodoDisperso(cadena, None, None, None, None, None)
			self.Cabecera.abajo = NodoDisperso(dato, None, None, None, None, None)
			self.actual = self.Cabecera.abajo
			self.tamano = self.tamano + 1
		else:
			self.actual.abajo = NodoDisperso(dato, None, None, None, None, None)


	


class FilaCorreos():
	def __init__(self, cabe):
		self.Cabecera = cabe
		self.actual = None
		self.tamano = 0

	def AgregarNodo(self, dato):
		return 'hola'

	

class ProfundidadCorreos():
	def __init__(self, ra):
		self.Raiz = ra
		self.actual = None
		self.tamano = 0

	def AgregarNodo(self, dato):
		return 'hola'


class Matriz():
	def __init__(self):
		self.X = 0
		self.Y = 0

	def AgregarNodo(self, dato):
		return 'hola'


#Nodo dato matriz-----------------------------------------------------------------------------------------------------------------------------------------
class NodoDisperso():
	def __init__(self, dat, arr, ab, der, iz, ad):
		self.dato = dat
		self.derecha = der
		self.izaquierda = iz
		self.arriba = arr
		self.abajo = ab
		self.adentro = ad




#Nodo-----------------------------------------------------------------------------------------------------------------------------------------------------
class Nodo():
	def __init__(self, dat, sig):
		self.dato = dat
		self.siguiente = sig
	
		


#fin------------------------------------------------------------------------------------------------------------------------------------------------------
lista = listaSimple()
pila = Pila()
cola = Cola()

@app.route("/GrafLista", methods=['POST'])
def RecLista():
	dato = str(request.form["dato"])
	aux = lista.recorrer(dato)
	return aux

@app.route("/GrafCola", methods=['POST'])
def RecCola():
	dato = str(request.form["dato"])
	aux = cola.recorrer(dato)
	return aux

@app.route("/GrafPila", methods=['POST'])
def RecPila():
	dato = str(request.form["dato"])
	aux = pila.recorrer(dato)
	return aux

@app.route("/AgregarSimple", methods=['POST'])
def add():
	dato = str(request.form["dato"])
	aux = lista.Agregar(dato)
	return aux

@app.route("/EliminarSimple", methods=['POST'])
def remove():
	dato = str(request.form["dato"])
	aux = lista.EliminarNodo(dato)
	return aux

@app.route("/BuscarSimple", methods=['POST'])
def search():
	dato = str(request.form["dato"])
	aux = lista.BuscarNodo(dato)
	return aux



@app.route("/Push", methods=['POST'])
def PushPila():
	dato = str(request.form["dato"])
	aux = pila.Push(dato)
	return aux

@app.route("/Pop", methods=['POST'])
def PopPila():
	dato = str(request.form["dato"])
	aux = pila.Pop(dato)
	return aux

@app.route("/QueueCola", methods=['POST'])
def queueCola():
	dato = str(request.form["dato"])
	aux = cola.Ingresar(dato)
	return aux

@app.route("/DeQueueCola", methods=['POST'])
def deQueueCola():
	dato = str(request.form["dato"])
	aux = cola.Sacar(dato)
	return aux



if __name__ == '__main__':
	app.run(debug=True)