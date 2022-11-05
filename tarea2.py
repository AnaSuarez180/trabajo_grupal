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

#OPCIÓN 1

#Quizás puedo aumentarle números al final del url hasta alcanzar el límite de la gen??
#Del 1 al 151 son gen 1

# #Generación 1
# def gen_uno():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 151}

#     for offfset in range(0, 152, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 2
# def gen_dos():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 100}

#     for offfset in range(151, 251, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 3
# def gen_tres():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 135}

#     for offfset in range(251, 386, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 4
# def gen_cuatro():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 107}

#     for offfset in range(386, 493, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 5
# def gen_cinco():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 156}

#     for offfset in range(493, 649, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 6
# def gen_seis():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 72}

#     for offfset in range(649, 721, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 7
# def gen_siete():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 88}

#     for offfset in range(721, 809, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# #Generación 8
# def gen_ocho():
#     url_api = 'https://pokeapi.co/api/v2/pokemon/'
#     params = {'limit': 96}

#     for offfset in range(809, 905, 200):
#         params['offset'] = offfset
#         response = requests.get(url_api, params=params)

#         if response.status_code != 200:
#             print(response.text)
#         else:
#             data = response.json()
#             for item in data['results']:
#                 print(item['name'])

# opcion_1 = input('Ingresa el número de la generación a listar: ')
# if int(opcion_1) == 1:
#     gen_uno()
# elif int(opcion_1) ==2:
#     gen_dos()
# elif int(opcion_1) == 3:
#     gen_tres()
# elif int(opcion_1) == 4:
#     gen_cuatro()
# elif int(opcion_1) == 5:
#     gen_cinco()
# elif int(opcion_1) == 6:
#     gen_seis()
# elif int(opcion_1) == 7:
#     gen_siete()
# elif int(opcion_1) == 8:
#     gen_ocho()
# else:
#     print('Opción incorrecta.')

#OPCIÓN 2
print('Formas disponibles:')
print('Pichu, Unown, Burmy, Cherrym, Shellos, Gastrodon, Arceus, Deerling, Sawsbuck,')
print('Genesect, Vivillon, Flabebe, Floette, Florges, Furfou, Xerneas, Silvally,')
print('Sinistea, Polteageist, Alcremie')

#FORM PICHU
def formar_pichu():
    pokemon_numbers = []
    for i in range(171, 173):
        pokemon_numbers.append(i)
    for id in pokemon_numbers:
        url_api = f'https://pokeapi.co/api/v2/pokemon/{id}/'
        response = requests.get(url_api)    
        if response.status_code != 200:
                print(response.text)
        else:
            data = response.json()        
            if len(data['forms']) >= 2:
                for item in data['forms']:
                    print(data['name'], item)
                
#FORM UNOWN
def formar_unown():
    url_api = 'https://pokeapi.co/api/v2/pokemon/201/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

# #FORM BURMY
def formar_burmy():
    url_api = 'https://pokeapi.co/api/v2/pokemon/412/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM CHERRIM
def formar_cherrim():
    url_api = 'https://pokeapi.co/api/v2/pokemon/421/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM SHELLOS
def formar_shellos():
    url_api = 'https://pokeapi.co/api/v2/pokemon/422/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM GASTRODON
def formar_gastrodon():
    url_api = 'https://pokeapi.co/api/v2/pokemon/423/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM ARCEUS
def formar_arceus():
    url_api = 'https://pokeapi.co/api/v2/pokemon/493/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM DEERLING
def formar_deerling():
    url_api = 'https://pokeapi.co/api/v2/pokemon/585/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM SAWSBUCK
def formar_sawsbuck():
    url_api = f'https://pokeapi.co/api/v2/pokemon/586/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM GENESECT
def formar_genesect():
    url_api = 'https://pokeapi.co/api/v2/pokemon/649/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM VIVILLON
def formar_vivillon():
    url_api = 'https://pokeapi.co/api/v2/pokemon/666/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM FLABEBE
def formar_flabebe():
    url_api = 'https://pokeapi.co/api/v2/pokemon/669/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM FLOETTE
def formar_floette():
    url_api = 'https://pokeapi.co/api/v2/pokemon/670/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM FLORGES
def formar_florges():
    url_api = 'https://pokeapi.co/api/v2/pokemon/671/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM FURFROU
def formar_furfrou():
    url_api = 'https://pokeapi.co/api/v2/pokemon/676/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM XERNEAS
def formar_xerneas():
    url_api = 'https://pokeapi.co/api/v2/pokemon/716/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM SILVALLY
def formar_silvally():
    url_api = 'https://pokeapi.co/api/v2/pokemon/773/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM SINISTEA
def formar_sinistea():
    url_api = 'https://pokeapi.co/api/v2/pokemon/854/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM POLTEAGEIST
def formar_polteageist():
    url_api = 'https://pokeapi.co/api/v2/pokemon/855/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

#FORM ALCREMIE
def formar_alcremie():
    url_api = 'https://pokeapi.co/api/v2/pokemon/869/'
    response = requests.get(url_api)    
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()        
        if len(data['forms']) >= 2:
            for item in data['forms']:
                print(data['name'], item)

opcion_2 = input('Ingresa el nombre de la forma a listar: ')

if opcion_2.lower() == 'pichu':
    formar_pichu()
elif opcion_2.lower() == 'unown':
    formar_unown()
elif opcion_2.lower() == 'burmy':
    formar_burmy()
elif opcion_2.lower() == 'cherrim':
    formar_cherrim()
elif opcion_2.lower() == 'shellos':
    formar_shellos()
elif opcion_2.lower() == 'gastrodon':
    formar_gastrodon()
elif opcion_2.lower() == 'arceus':
    formar_arceus()
elif opcion_2.lower() == 'deerling':
    formar_deerling()
elif opcion_2.lower() == 'sawsbuck':
    formar_sawsbuck()
elif opcion_2.lower() == 'genesect':
    formar_genesect()
elif opcion_2.lower() == 'vivillon':
    formar_vivillon()
elif opcion_2.lower() == 'flabebe':
    formar_flabebe()
elif opcion_2.lower() == 'floette':
    formar_floette()
elif opcion_2.lower() == 'florges':
    formar_florges()
elif opcion_2.lower() == 'furfrou':
    formar_furfrou()
elif opcion_2.lower() == 'xerneas':
    formar_xerneas()
elif opcion_2.lower() == 'silvally':
    formar_silvally()
elif opcion_2.lower() == 'sinistea':
    formar_sinistea()
elif opcion_2.lower() == 'polteageist':
    formar_polteageist()
elif opcion_2.lower() == 'alcremie':
    formar_alcremie()
else:
    print('Opción incorrecta.')
