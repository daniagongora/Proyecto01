import requests
import json
import csv
from io import open

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
		
	datosDelClima=peticiones[iata]

	temperatura=str(datosDelClima["main"]["temp"])
	humedad=str(datosDelClima["main"]["humidity"])
	sensacion=str(datosDelClima["main"]["feels_like"])
	presion=str(datosDelClima["main"]["pressure"])
		
	datoTemperatura=iata+"\n lugar: "+datosDelClima["name"]+"\n temperatura: "+temperatura
	datoHumedad="\n humedad: "+humedad+"\n descripcion: "+datosDelClima["weather"][0]["description"]
	datoSensacion="\n con sensación de: "+sensacion+"\n presion: "+presion
	informacion=datoTemperatura+datoHumedad+datoSensacion
		
			
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
		
	for row in reader:
		origen.append(row[0])
		destino.append(row[1])
		
	for i in origen[2:]:
			
		for j in destino[2:]:
				
			climaOrigen=diccionario[i]
			climaDestino=diccionario[j]
				
			temperatura=str(climaOrigen["main"]["temp"])
			humedad=str(climaOrigen["main"]["humidity"])
			sensacion=str(climaOrigen["main"]["feels_like"])
			presion=str(climaOrigen["main"]["pressure"])

			temperatura2=str(climaDestino["main"]["temp"])
			humedad2=str(climaDestino["main"]["humidity"])
			sensacion2=str(climaDestino["main"]["feels_like"])
			presion2=str(climaDestino["main"]["pressure"])
				
			print(
				i+"\n lugar: "+climaOrigen["name"]+"\n temperatura: "+temperatura+
				"\n humedad: "+humedad+"\n descripcion: "+climaOrigen["weather"][0]["description"]+
				"\n con sensación de: "+sensacion+"\n presion: "+presion
				)

			print(
				j+"\n lugar: "+climaDestino["name"]+"\n temperatura: "+temperatura2+
				"\n humedad: "+humedad2+"\n descripcion: "+climaDestino["weather"][0]["description"]+
				"\n con sensación de: "+sensacion2+"\n presion: "+presion2
				)

def main():
	"""
	Ejecuta el proyecto completo
	"""

	leerBoletos(peticiones(lecturaCache()))
	
if __name__=="__main__":

	main()