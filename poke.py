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