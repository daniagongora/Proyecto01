import requests
import json
import csv
from io import open

"""
Programa que se encarga de hacer lo que pide el proyecto 1
"""

"""
ENTRADA
"""

class Proyecto01:
	
	"""
	Método para las peticiones
	"""
	def peticiones(diccionario):
		
		#diccionario nuevo para almacenar las ciudades con su clima
		diccionarioClima={} 
	
		#llave de la api (esta es la de mi cuenta, pueden probar con otra de preferncia)
		llaveApi="87dd4d6b93bcf3872531c2fecaf51962"
		url="http://api.openweathermap.org/data/2.5/weather?"

		#por cada ciudad en el diccionario de lectura hace una petición 
		for clave in diccionario.keys():
			
			peticionApi=url+"lat="+diccionario[clave][0]+"&"+"lon="+diccionario[clave][1]+"&units=metric&lang=es&appid="+llaveApi

			peticion=requests.get(peticionApi)
			
			#guardar las peticiones en json para despues manejarlas, en el diccionario nuevo
			if peticion.status_code!=404:
				diccionarioClima[clave]=peticion.json() 
				

		return diccionarioClima

	"""
	Método para leer el csv para almacenar los datos en un diccionario(cache) el cual 
	se podra consultar
	"""
	def lecturaCache():
	
		#el cache donde se almacenara la información
		cache={}
	
		#con DictReader puedo abrir el csv e iterar para leer más facilmente en un diccionario
		documento = csv.DictReader(open("entrada/dataset1.csv"))
	
		for row in documento:
			#guardara las coordenadas de cada ciudad de origen en una lista
			origenCoordenadas=[row["origin_latitude"],row["origin_longitude"]]
			ciudadOrigen=row["origin"]

			#guardara las coordenadas de cada ciudad de destino en una lista
			destinoCoordenadas=[row["destination_latitude"],row["destination_longitude"]]
			ciudadDestino=row["destination"]

			#guardara con las claves de ciudades sus coordenadas
			cache[ciudadOrigen]=origenCoordenadas
			cache[ciudadDestino]=destinoCoordenadas

	
		return cache
"""
SALIDA
"""

		"""
		Método que mostrara los datos del clima de la ciudad dada con su iata
		la información la consultara con lo guardado en el diccionario de
		peticiones
		"""
	
	def salidaClima(peticiones,iata):

		#almacena los datos del clima
		datos=peticiones[iata]

		#convierte en string los datos para poder mostrarlos
		temperatura=str(datos["main"]["temp"])
		humedad=str(datos["main"]["humidity"])
		sensacion=str(datos["main"]["feels_like"])
		presion=str(datos["main"]["pressure"])
		
		"""
		Método para mostrar los datos de cada ciudad en el orden que aparece en el .csv de acuerdo a los boletos
		"""
		
		print(
			iata+"\n lugar: "+datos["name"]+"\n temperatura: "+temperatura+
			"\n humedad: "+humedad+"\n descripcion: "+datos["weather"][0]["description"]+
			"\n con sensación de: "+sensacion+"\n presion: "+presion
			)
	
