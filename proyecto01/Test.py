from Proyecto01 import *
import requests

class Test:
	""" 
	pruebas para el proyecto01
	"""
	
	def pruebaPeticiones():
		"""
		método para probar las peticiones al OpenweatherMap
		se hagan de la manera correcta
		"""
		
		diccionarioPrueba={"MEX":["123","456"]}
		assert(Proyecto01.peticiones(diccionarioPrueba)!=200)

	
	def pruebaLecturaCache():
		"""
		método para probar que se lee correctamente el documento y el cache 
		funciona adecuadamente
		"""

		diccionarioPrueba=["49.0128","2.55"]
		assert(Proyecto01.lecturaCache()["CDG"]==diccionarioPrueba)

	
	def pruebaSalidaClima():
		"""
    	        método para probar que el método salidaClima, imprime en el
        	formato correcto
        	"""
    	
        	diccionarioPrueba1 = Proyecto01.lecturaCache()
        	diccionarioPrueba2 = Proyecto01.peticiones(diccionarioPrueba1)
        	assert("lugar","temperatura","humedad","sensacion" in Proyecto01.salidaClima(diccionarioPrueba2))

