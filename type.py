url_api_5 = "https://pokeapi.co/api/v2/type/"

import requests


def type_0(type_name):
    response = requests.get(url_api_5+ type_name)
    
    data = response.json()
    
    #lista de pokemones en habitat
    
    type_pokemones = [tipo['pokemon']['name']for tipo in data['pokemon']]

    for i in range(len(type_pokemones)):
        print("Pokemon: {}".format(type_pokemones[i]))
        
              
opcion_5 = input('Ingresa el tipo del pokemon a listar: ')
if str(opcion_5) == "normal":
    type_0("normal")
elif str(opcion_5) == "fighting":
    type_0("fighting")
elif str(opcion_5) == "flying":
    type_0("flying")
elif str(opcion_5) == "poison":
    type_0("poison")
elif str(opcion_5) == "ground":
    type_0("ground")
elif str(opcion_5) == "rock":
    type_0("rock")
elif str(opcion_5) == "bug":
    type_0("bug")
elif str(opcion_5) == "ghost":
    type_0("ghost")
elif str(opcion_5) == "steel":
    type_0("steel")
elif str(opcion_5) == "fire":
    type_0("fire")
elif str(opcion_5) == "water":
    type_0("water")
elif str(opcion_5) == "grass":
    type_0("grass")
elif str(opcion_5) == "electric":
    type_0("electric")
elif str(opcion_5) == "psychic":
    type_0("psychic")
elif str(opcion_5) == "ice":
    type_0("ice")
elif str(opcion_5) == "dragon":
    type_0("dragon")
elif str(opcion_5) == "dark":
    type_0("dark")
elif str(opcion_5) == "fairy":
    type_0("fairy")
elif str(opcion_5) == "unknown":
    type_0("unknown")
elif str(opcion_5) == "shadow":
    type_0("shadow")
else:
    print('Tipo Incorrecto, elige otro por favor.')