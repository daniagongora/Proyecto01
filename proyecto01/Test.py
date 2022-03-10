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
	método para probar que el método salidaClima imprime en el formato correcto
	"""
	def pruebaSalidaClima():
                
		#se comprobará que la salida imprima correctamente las palabras clave que debe imprimir.

                
                diccionarioPrueba1 = Proyecto01.lecturaCahe()
                diccionarioPrueba2 = Proyecto01.peticiones(diccionarioPrueba1)
                assert("lugar","temperatura","humedad","sensacion" in Proyecto01.salidaClima(diccionarioPrueba2)))		

		
