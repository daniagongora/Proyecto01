from Proyecto01 import salidaClima
from Proyecto01 import peticiones
from Proyecto01 import lecturaCache
import requests
import json

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
		assert(peticiones(diccionarioPrueba)!=200)

	
	def pruebaLecturaCache():
		"""
		método para probar que se lee correctamente el documento y el cache 
		funciona adecuadamente
		"""

		diccionarioPrueba=["49.0128","2.55"]
		assert(lecturaCache()["CDG"]==diccionarioPrueba)

	def pruebaSalidaClima():
		"""
		método para probar que salidaClima arroja los datos correctos
		"""
		llaveApi="87dd4d6b93bcf3872531c2fecaf51962"
		url="http://api.openweathermap.org/data/2.5/weather?"

		peticionApi=url+"lat=25.7785"+"&"+"lon=-100.107"+"&units=metric&lang=es&appid="+llaveApi

		peticion=requests.get(peticionApi)
		diccionarioPrueba={"MTY":peticion.json()}

		assert("temperatura" in salidaClima(diccionarioPrueba,"MTY"))
		assert("humedad" in salidaClima(diccionarioPrueba,"MTY"))
		assert("lugar" in salidaClima(diccionarioPrueba,"MTY"))
		assert("sensación" in salidaClima(diccionarioPrueba,"MTY"))

	