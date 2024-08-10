import requests
from Especie import Especie
from Pelicula import Pelicula
from Planeta import Planeta
from Personaje import Personaje
from Nave import Nave
import matplotlib.pyplot as plt

BASEURL = "https://www.swapi.tech/api/"

def fetch_data(endpoint):
    response = requests.get(f"{BASEURL}{endpoint}")
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return data["result"]
        elif "results" in data:
            return data["results"]
        else:
            print(f"Respuesta equivocada {endpoint}: {data}")
            return None
    else:
        print(f"Fallo al hacer fetch {endpoint}, status code: {response.status_code}")
        return None

def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return data["result"]
        elif "results" in data:
            return data["results"]
        else:
            print(f"Respuesta equivocada para el URL {url}: {data}")
            return None
    else:
        print(f"Fallo al hacer fetch {url}, status code: {response.status_code}")
        return None

def get_films():
    films_data = fetch_data("films")
    films = []
    for film_data in films_data:
        properties = film_data["properties"]
        film = Pelicula(properties["title"], properties["episode_id"], properties['release_date'], properties["opening_crawl"], properties["director"])
        films.append(film)
    return films

def get_species():
    species_data = fetch_data("species")
    species_list = []
    for species_item in species_data:
        detailed_species_data = fetch_data_from_url(species_item["url"])
        properties = detailed_species_data["properties"]

        characters = []
        for character_url in properties.get("people", []):
            character_data = fetch_data_from_url(character_url)
            if character_data:
                characters.append(character_data["properties"]["name"])

        films_data = fetch_data("films")
        films = []
        for film_data in films_data:
            film_properties = film_data["properties"]
            if "species" in film_properties:
                if species_item["url"] in film_properties["species"]:
                    films.append(film_properties["title"])

        homeworld_name = "Unknown"
        if properties.get("homeworld"):
            homeworld_data = fetch_data_from_url(properties["homeworld"])
            if homeworld_data and "properties" in homeworld_data and "name" in homeworld_data["properties"]:
                homeworld_name = homeworld_data["properties"]["name"]

        species = Especie(
            properties["name"],
            properties["average_height"],
            properties["classification"],
            homeworld_name,
            properties["language"],
            characters,
            films
        )
        species_list.append(species)
    return species_list

def get_planets():
    planets_data = fetch_data("planets")
    planets = []
    for planet_data in planets_data:
        if "properties" not in planet_data:
            print(f"Fetching detailed data for planet: {planet_data['name']}")
            detailed_planet_data = fetch_data_from_url(planet_data["url"])
            if detailed_planet_data and "properties" in detailed_planet_data:
                planet_data["properties"] = detailed_planet_data["properties"]
            else:
                print(f"Skipping planet data without 'properties': {planet_data}")
                continue

        properties = planet_data["properties"]

        films_data = fetch_data("films")
        films = []
        for film_data in films_data:
            film_properties = film_data["properties"]
            if "planets" in film_properties:
                if planet_data["url"] in film_properties["planets"]:
                    films.append(film_properties["title"])

        characters = []
        for resident_url in properties.get("residents", []):
            character_data = fetch_data_from_url(resident_url)
            if character_data and "properties" in character_data:
                characters.append(character_data["properties"]["name"])

        planet = Planeta(
            properties["name"],
            properties["orbital_period"],
            properties["rotation_period"],
            properties["population"],
            properties["climate"],
            films,
            characters
        )
        planets.append(planet)
    return planets

species = get_species()
for specie in species:
    print(specie)