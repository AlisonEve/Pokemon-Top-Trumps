import random
import requests


def pokemon_chooser():
    poke_id = random.randint(1, 152)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_id)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_info = {"Name": pokemon["name"], "ID": poke_id, "Height": pokemon["height"], "Weight": pokemon["weight"]}
    return pokemon_info