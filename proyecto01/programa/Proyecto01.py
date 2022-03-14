import requests
import json
import csv
from io import open


class Proyecto01:

	"""
	Clase que se encarga de hacer lo que pide el proyecto 1
	"""	
	
	def peticiones(diccionario):
		"""
		Método para las peticiones
		"""	
		diccionarioClima={} 
	
		llaveApi="87dd4d6b93bcf3872531c2fecaf51962"
		url="http://api.openweathermap.org/data/2.5/weather?"

		for clave in diccionario.keys():
			
			peticionApi=url+"lat="+diccionario[clave][0]+"&"+"lon="+diccionario[clave][1]+"&units=metric&lang=es&appid="+llaveApi

			peticion=requests.get(peticionApi)
			
			if peticion.status_code!=404:
				diccionarioClima[clave]=peticion.json() 
				

		return diccionarioClima

	
	def lecturaCache():
		"""
		Método para leer el csv para almacenar los datos en un diccionario(cache) el cual 
		se podra consultar
		"""
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

		
	def salidaClima(peticiones,iata):
		"""
		Método que mostrara los datos del clima de la ciudad dada con su iata
		la información la consultara con lo guardado en el diccionario de
		peticiones
		"""
		
		datos=peticiones[iata]

		temperatura=str(datos["main"]["temp"])
		humedad=str(datos["main"]["humidity"])
		sensacion=str(datos["main"]["feels_like"])
		presion=str(datos["main"]["pressure"])
		
		linea1=iata+"\n lugar: "+datos["name"]+"\n temperatura: "+temperatura
		linea2="\n humedad: "+humedad+"\n descripcion: "+datos["weather"][0]["description"]
		linea3="\n con sensación de: "+sensacion+"\n presion: "+presion
		informacion=linea1+linea2+linea3
		
		print(informacion)
		return informacion
	
