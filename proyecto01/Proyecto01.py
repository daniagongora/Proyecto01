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
		
		string1=iata+"\n lugar: "+datos["name"]+"\n temperatura: "+temperatura
		string2="\n humedad: "+humedad+"\n descripcion: "+datos["weather"][0]["description"]
		string3="\n con sensación de: "+sensacion+"\n presion: "+presion
		informacion=string1+string2+string3
		
			
		print(informacion)
		return informacion
	

	def leerBoletos(diccionarioPeticion):
		"""
		Método que muestra los datos del clima
		de los 3000 boletos
		"""

		diccionario=diccionarioPeticion
		dataset=open("entrada/dataset1.csv")
		reader = csv.reader(dataset)
		origen=["lista"]
		destino=["lista"]
		s=0
		for row in reader:
			origen.append(row[0])
			destino.append(row[1])
		
		for i in origen[2:]:
			
			for j in destino[2:]:
				
				datos=diccionario[i]
				datos2=diccionario[j]
				
				temperatura=str(datos["main"]["temp"])
				humedad=str(datos["main"]["humidity"])
				sensacion=str(datos["main"]["feels_like"])
				presion=str(datos["main"]["pressure"])

				temperatura2=str(datos2["main"]["temp"])
				humedad2=str(datos2["main"]["humidity"])
				sensacion2=str(datos2["main"]["feels_like"])
				presion2=str(datos2["main"]["pressure"])
				s=s+1
				x=str(s)
				print("el número: "+x)
				print(
					i+"\n lugar: "+datos["name"]+"\n temperatura: "+temperatura+
					"\n humedad: "+humedad+"\n descripcion: "+datos["weather"][0]["description"]+
					"\n con sensación de: "+sensacion+"\n presion: "+presion
				)

				print(
					j+"\n lugar: "+datos2["name"]+"\n temperatura: "+temperatura2+
					"\n humedad: "+humedad2+"\n descripcion: "+datos2["weather"][0]["description"]+
					"\n con sensación de: "+sensacion2+"\n presion: "+presion2
				)

	leerBoletos(peticiones(lecturaCache()))