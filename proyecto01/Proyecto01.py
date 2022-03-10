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
		
		diccionarioClima={} 
	
		#llave de la api (esta es la de mi cuenta, pueden probar con otra de preferncia)
		llaveApi="87dd4d6b93bcf3872531c2fecaf51962"
		url="http://api.openweathermap.org/data/2.5/weather?"

		for clave in diccionario.keys():
			
			peticionApi=url+"lat="+diccionario[clave][0]+"&"+"lon="+diccionario[clave][1]+"&units=metric&lang=es&appid="+llaveApi

			peticion=requests.get(peticionApi)
			
			if peticion.status_code!=404:
				diccionarioClima[clave]=peticion.json() 
				

		return diccionarioClima

	"""
	Método para leer el csv para almacenar los datos en un diccionario(cache) el cual 
	se podra consultar
	"""
	def lecturaCache():
	
		cache={}

		documento = csv.DictReader(open("entrada/dataset1.csv"))
	
		for row in documento:
			
			origenCoordenadas=[row["origin_latitude"],row["origin_longitude"]]
			ciudadOrigen=row["origin"]

			
			destinoCoordenadas=[row["destination_latitude"],row["destination_longitude"]]
			ciudadDestino=row["destination"]

			
			cache[ciudadOrigen]=origenCoordenadas
			cache[ciudadDestino]=destinoCoordenadas

	
		return cache

		"""
		Método que mostrara los datos del clima de la ciudad dada con su iata
		la información la consultara con lo guardado en el diccionario de
		peticiones
		"""
	def salidaClima(peticiones,iata):

		#almacena los datos del clima
		datos=peticiones[iata]

		temperatura=str(datos["main"]["temp"])
		humedad=str(datos["main"]["humidity"])
		sensacion=str(datos["main"]["feels_like"])
		presion=str(datos["main"]["pressure"])
		
		string1=iata+"\n lugar: "+datos["name"]+"\n temperatura: "+temperatura
		string2="\n humedad: "+humedad+"\n descripcion: "+datos["weather"][0]["description"]
		string3="\n con sensación de: "+sensacion+"\n presion: "+presion
		informacion=string1+string2+string3
		
			
		print(informacion)
		return informacion
	
