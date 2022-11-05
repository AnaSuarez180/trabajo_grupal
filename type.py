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
else:
    print('Tipo Incorrecto, elige otro por favor.')
     