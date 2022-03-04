import requests
import json
import csv
from io import open
"""
Programa que se encarga de hacer lo que pide el proyecto 1
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

		#por cada ciudad en el diccionario de lectura hace una petición 
		for ciudadOrigen in diccionario.keys():

			peticionApi="http://api.openweathermap.org/data/2.5/weather?" + "lat=" +diccionario[ciudadOrigen][0]+"&"+"lon="+diccionario[ciudadOrigen][1]+"&units=metric&appid="+llaveApi

			peticion=requests.get(peticionApi)

		for ciudadDestino in diccionario.keys():

			peticionApi2="http://api.openweathermap.org/data/2.5/weather?" + "lat=" +diccionario[ciudadDestino][0]+"&"+"lon="+diccionario[ciudadDestino][1]+"&units=metric&appid="+llaveApi
			peticion2=requests.get(peticionApi2)

		#guardar las peticiones en json para despues manejarlas, en el diccionario nuevo
		if peticion.status_code==200 and peticion2.status_code == 200:
			diccionarioClima[ciudadOrigen]=peticion.json() 
			diccionarioClima[ciudadDestino]=peticion.json()


		return peticion.status_code+peticion2.status_code 

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
