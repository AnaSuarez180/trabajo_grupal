"""La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 
y el paquete requests de Python

Escribir un programa que tenga las siguientes opciones:

Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) 
y se listan todos los pokemon respectivos.
Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) 
y se listan todos los pokemons respectivos.
Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar 
para interactuar.
Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar 
para interactuar.
Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar 
para interactuar.
Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen"""

import requests


url_api = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url_api)
data = response.json()

#Quizás puedo aumentarle números al final del url hasta alcanzar el límite de la gen??
#Del 1 al 151 son gen 1

#Generación 1
url_api = 'https://pokeapi.co/api/v2/pokemon/'
params = {'limit': 151}

for offfset in range(0, 152, 200):
    params['offset'] = offfset
    response = requests.get(url_api, params=params)

    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        for item in data['results']:
            print(item['name'])



# def get_pokemon(gen):
#     if gen == 'gen 1': 
#         for number in range(0, 152):
#             str(number)
#         com_url = [number for number in range(0, 152)]
#         for number in com_url:
#             response_api = requests.get(url_api + str(number))
#     data = response_api.json()
    
    
#     lista_nombres = {data['names'][0]['name']} #Solo me sale el 151 :(
    
#     print(f'Nombres:{lista_nombres}')

# get_pokemon('gen 1')



