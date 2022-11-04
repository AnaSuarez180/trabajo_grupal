url_api = "https://pokeapi.co/api/v2/pokemon-habitat/"

import requests


def habitat(habitat_name):
    response = requests.get(url_api+ habitat_name)
    
    data = response.json()
    
    #lista de pokemones en habitat
    
    lista_pokemones = [pokemones['name']for pokemones in data['pokemon_species']]
    
    print(f"Pokemones en este habitat: {lista_pokemones}")
    
opcion_2 = input('Ingresa el número del Habitat a listar: ')
if str(opcion_2) == "cave":
    habitat("cave")
if str(opcion_2) == "forest":
    habitat("forest")
if str(opcion_2) == "grassland":
    habitat("grassland")
if str(opcion_2) == "mountain":
    habitat("mountain")
if str(opcion_2) == "rare":
    habitat("rare")
if str(opcion_2) == "rough-terrain":
    habitat("rough-terrain")
if str(opcion_2) == "sea":
    habitat("sea")
if str(opcion_2) == "urban":
    habitat("urban")
if str(opcion_2) == "waters-edge":
    habitat("waters-edge")

else:
    print('Habitat Incorrecto, elige otro por favor.')