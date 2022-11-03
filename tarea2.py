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
def gen_uno():
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

#Generación 2
def gen_dos():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 100}

    for offfset in range(151, 251, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 3
def gen_tres():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 135}

    for offfset in range(251, 386, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 4
def gen_cuatro():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 107}

    for offfset in range(386, 493, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 5
def gen_cinco():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 156}

    for offfset in range(493, 649, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 6
def gen_seis():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 72}

    for offfset in range(649, 721, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 7
def gen_siete():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 88}

    for offfset in range(721, 809, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

#Generación 8
def gen_ocho():
    url_api = 'https://pokeapi.co/api/v2/pokemon/'
    params = {'limit': 96}

    for offfset in range(809, 905, 200):
        params['offset'] = offfset
        response = requests.get(url_api, params=params)

        if response.status_code != 200:
            print(response.text)
        else:
            data = response.json()
            for item in data['results']:
                print(item['name'])

opcion_1 = input('Ingresa el número de la generación a listar: ')
if int(opcion_1) == 1:
    gen_uno()
elif int(opcion_1) ==2:
    gen_dos()
elif int(opcion_1) == 3:
    gen_tres()
elif int(opcion_1) == 4:
    gen_cuatro()
elif int(opcion_1) == 5:
    gen_cinco()
elif int(opcion_1) == 6:
    gen_seis()
elif int(opcion_1) == 7:
    gen_siete()
elif int(opcion_1) == 8:
    gen_ocho()
else:
    print('Opción incorrecta.')