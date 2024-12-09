import requests
import json

api_url = "https://pokeapi.co/api/v2"

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    # TODO: Fetch data for both Pokémon
    url1 = api_url+"/pokemon/" + pokemon1
    url2 = api_url + "/pokemon/" + pokemon2
    pokemon1_api_data = requests.get(url1)
    pokemon1_api_data = pokemon1_api_data.json()
    pokemon1_api_data = pokemon1_api_data["stats"]
    pokemon2_api_data = requests.get(url2)
    pokemon2_api_data = pokemon2_api_data.json()
    pokemon2_api_data = pokemon2_api_data["stats"]
    # TODO: Calculate stats at level 50 for both Pokémon
    pokemon1 = {
        'name': pokemon1,
        'hp': calculate_hp(pokemon1_api_data[0]['base_stat']), 'stats':
        [{'stat': {'name':'speed'}, 'base_stat': calculate_stat(pokemon1_api_data[5]['base_stat'])},
        {'stat': {'name':'attack'}, 'base_stat': calculate_stat(pokemon1_api_data[1]['base_stat'])},
        {'stat': {'name':'defense'}, 'base_stat': calculate_stat(pokemon1_api_data[2]['base_stat'])}]
        }
    pokemon2 = {
        'name': pokemon2,
        'hp': calculate_hp(pokemon2_api_data[0]['base_stat']), 'stats':
        [{'stat': {'name':'speed'}, 'base_stat': calculate_stat(pokemon2_api_data[5]['base_stat'])},
        {'stat': {'name':'attack'}, 'base_stat': calculate_stat(pokemon2_api_data[1]['base_stat'])},
        {'stat': {'name':'defense'}, 'base_stat': calculate_stat(pokemon2_api_data[2]['base_stat'])}]
        }
    print(pokemon2["hp"])
    # TODO: Determine which Pokémon attacks first based on speed
    if pokemon1["stats"][0]["base_stat"] > pokemon2["stats"][0]["base_stat"]:
        battle(pokemon1,pokemon2)
    else:
        battle(pokemon2,pokemon1)

def calculate_damage(attacker, defender, level=50, base_power=60):
    return int(((2*level*0.4+2) * attacker['stats'][1]['base_stat'] * base_power) / (defender['stats'][2]['base_stat'] * 50) + 2)

def battle(pokemon1, pokemon2):
    turn = 1
    while pokemon1['hp'] > 0 and pokemon2['hp'] > 0:
        pokemon2['hp'] -= calculate_damage(pokemon1, pokemon2)
        print(pokemon2["name"],"has",pokemon2["hp"],"left on turn",turn)
        if pokemon2['hp'] <= 0:
            print(f"{pokemon1['name']} wins!","on turn",turn)
            print(pokemon1["name"],"has",pokemon1["hp"],"remaining")
            break
            # Swap roles 
        turn += 1          
        pokemon1, pokemon2 = pokemon2, pokemon1

# Example usage
simulate_battle("eevee","jigglypuff")