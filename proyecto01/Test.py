import proyecto01

""" 
pruebas para el proyecto01, sugiero que el archivo donde se haga el proyecto 
se llame proyecto01 y ahi se almacenen los métodos
por lo que supondre que asi se llama, si le ponen otro nombre 
solo sustituyanlo
"""

class Test:
	
	"""
	método para probar las peticiones al OpenweatherMap
	se hagn de la manera correcta
	estoy suponiendo que el método se llama peticiones y no recibe argumentos 
	pero si no es así cambiar el nombre y agregar argumentos.
	probar con el comando python3 Test.py
	"""
	def pruebaPeticiones():
		
		#es 200 porque para API code eso significa que la petición se ha hecho correctamente
		#con 404 y 401 es que la peticion ssalio mal por eso debe salir diferente
		#por ahora que el método regrese el status code 
		
		assert(proyecto01.peticiones()==200)
		assert(proyecto01.peticiones()!=401)
		assert(proyecto01.peticiones()!=404)