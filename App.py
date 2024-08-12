import requests
from Especie import Especie
from Pelicula import Pelicula

BASEURL = "https://swapi.dev/api/"

def cargar_datos(endpoint):
    url = f"{BASEURL}{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def cargar_peliculas():
    films_data = cargar_datos("films/")
    if films_data:
        films = []
        for film_data in films_data["results"]:
            film = Pelicula(
                film_data["title"],
                film_data["episode_id"],
                film_data["director"],
                film_data["producer"],
                film_data["release_date"]
            )
            films.append(film)
        return films

# peliculas = cargar_peliculas()
# for pelicula in peliculas:
#     print(pelicula)

def cargar_especies():
    species_data = cargar_datos("species/")
    if species_data:
        species_list = []
        for species_item in species_data["results"]:
            species = Especie(
                species_item["name"],
                species_item["average_height"],
                species_item["classification"],
                species_item["homeworld"],
                species_item["language"],
                species_item["people"],
                species_item["films"]
            )
            species_list.append(species)
        return species_list

especies = cargar_especies()
for especie in especies:
    print(especie)