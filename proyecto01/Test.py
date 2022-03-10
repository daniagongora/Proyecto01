import Proyecto01
import requests

""" 
pruebas para el proyecto 1
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

	"""
	método para probar que se pueden visualizar los elementos del clima
	"""
	def pruebaSalidaClima():
		#se comprobará que la salida arroje correctamente valores string para ser vistos en pantalla
		
		stringP1="MXN,MTY \n 25°C \n"
		stringP2="47% de humedad \n "
		stringP3="sensación de 27° \n y presion de 1012hPa"
		informacionPrueba=stringP1+stringP2+stringP3
		assert(type(informacionPrueba.salidaClima())==str)
		
		
