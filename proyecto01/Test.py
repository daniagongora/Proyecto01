import Proyecto01
import requests

""" 
pruebas para el proyecto01, sugiero que el archivo donde se haga el proyecto 
se llame proyecto01 y ahi se almacenen los métodos
por lo que supondre que asi se llama, si le ponen otro nombre 
solo sustituyanlo
"""

class Test:
	
	"""
	método para probar las peticiones al OpenweatherMap
	se hagan de la manera correcta
	"""
	def pruebaPeticiones():
		
		#el método suma los status_code, si todo está bien regresa 400
		#si algo sale mal, regresa algo difrerente a 400, por lo que
		#si hace esta consulta incorrecta, deberia ser diferente de 400
		diccionarioPrueba={"MEX":["123","456"]}
		assert(Proyecto01.peticiones(diccionarioPrueba).status_code!=200)

	"""
	método para probar que se lee correctamente el documento y el cache 
	funciona adecuadamente
	"""
	def pruebaLecturaCache():

		#prueba que el valor asociado sea el correcto, es decir la long y lat correctas

		diccionarioPrueba=["49.0128","2.55"]
		assert(Proyecto01.lecturaCache()["CDG"]==diccionarioPrueba)

	