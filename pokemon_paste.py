import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    pokemon_name = pokemon_name.lower()

    # Build a clean URL and use it to send a GET request
    url = POKE_API_URL + pokemon_name
    response = requests.get(url)

    # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response.status_code == 200:
        return response.json()

    # If the GET request failed, print the error reason and return None
    print(f"Error: {response.status_code} - {response.reason}")
    return None