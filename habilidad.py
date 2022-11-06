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
if str(opcion_3) == "drizzle":
    habilidades_0("drizzle")
if str(opcion_3) == "speed-boost":
    habilidades_0("speed-boost")
if str(opcion_3) == "battle-armor":
    habilidades_0("battle-armor")
if str(opcion_3) == "sturdy":
    habilidades_0("sturdy")
