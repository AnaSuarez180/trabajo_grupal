url_api_4 = "https://pokeapi.co/api/v2/pokemon-habitat/"

import requests


def habitat(habitat_name):
    response = requests.get(url_api_4+ habitat_name)
    
    data = response.json()
    
    #lista de pokemones en habitat
    
    lista_pokemones = [pokemones['name']for pokemones in data['pokemon_species']]
      
    for i in range(len(lista_pokemones)):
        print("pokemon: {}".format(lista_pokemones[i]))
    
opcion_4 = input('Ingresa el nombre del Habitat a listar: ')
if str(opcion_4) == "cave":
    habitat("cave")
elif str(opcion_4) == "forest":
    habitat("forest")
elif str(opcion_4) == "grassland":
    habitat("grassland")
elif str(opcion_4) == "mountain":
    habitat("mountain")
elif str(opcion_4) == "rare":
    habitat("rare")
elif str(opcion_4) == "rough-terrain":
    habitat("rough-terrain")
elif str(opcion_4) == "sea":
    habitat("sea")
elif str(opcion_4) == "urban":
    habitat("urban")
elif str(opcion_4) == "waters-edge":
    habitat("waters-edge")
else:
    print('Habitat Incorrecto, elige otro por favor.')
    
