url_api_3 = "https://pokeapi.co/api/v2/ability/"

import requests

def habilidades_0(ability_name):
    response = requests.get(url_api_3+ ability_name)
    
    data = response.json()

    #lista de habilidades de pokemones
    
    habilidades_pokemones = [habilidad['pokemon']['name']for habilidad in data['pokemon']]

    for i in range(len(habilidades_pokemones)):
        print("Pokemon: {}".format(habilidades_pokemones[i]))

opcion_3 = input('Ingresa la habilidad del pokemon a listar: ')
if str(opcion_3) == "stench":
    habilidades_0("stench")