import Proyecto01
import requests

""" 
pruebas para el proyecto01
"""

class Test:
	
	"""
	método para probar las peticiones al OpenweatherMap
	se hagan de la manera correcta
	"""
	def pruebaPeticiones():

		diccionarioPrueba={"MEX":["123","456"]}
		assert(Proyecto01.peticiones(diccionarioPrueba).status_code!=200)

	"""
	método para probar que se lee correctamente el documento y el cache 
	funciona adecuadamente
	"""
	def pruebaLecturaCache():

		diccionarioPrueba=["49.0128","2.55"]
		assert(Proyecto01.lecturaCache()["CDG"]==diccionarioPrueba)

	"""
	método para probar que el método salidaClima()
	"""
	def salidaClima():

		assert("humedad" in Proyecto01.salidaClima(Proyecto01.peticiones(lecturaCache()),"MEX"))