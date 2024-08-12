import requests
from Especie import Especie
from Pelicula import Pelicula
from Planeta import Planeta
from Personaje import Personaje

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

# especies = cargar_especies()
# for especie in especies:
#     print(especie)

def cargar_planetas():
    planets_data = cargar_datos("planets/")
    if planets_data:
        planets_list = []
        for planet_item in planets_data["results"]:
            planet = Planeta(
                planet_item["name"],
                planet_item["orbital_period"],
                planet_item["rotation_period"],
                planet_item["population"],
                planet_item["climate"],
                planet_item["films"],
                planet_item["residents"]
            )
            planets_list.append(planet)
        return planets_list


# planetas = cargar_planetas()
# for planeta in planetas:
#     print(planeta)

def cargar_personajes():
    personajes_data = cargar_datos("people/")
    if personajes_data:
        personajes_list = []
        for personaje_item in personajes_data["results"]:
            personaje = Personaje(
                personaje_item["name"],
                personaje_item["homeworld"],
                personaje_item["films"],
                personaje_item["gender"],
                personaje_item["species"],
                personaje_item["starships"],
                personaje_item["vehicles"]
            )
            personajes_list.append(personaje)
        return personajes_list


# personajes = cargar_personajes()
# for personaje in personajes:
#     print(personaje)



def buscar_personajes():
    # Pedirle al usuario que escriba el nombre o una letra del nombre del personaje
    nombre_o_letra = input("Escribe el nombre o una letra del nombre del personaje: ").strip().lower()

    # Cargar los personajes
    personajes = cargar_personajes()

    # Filtro
    personajes_filtrados = [personaje for personaje in personajes if nombre_o_letra in personaje.nombre.lower()]

    # Mostrar los personajes
    if personajes_filtrados:
        for personaje in personajes_filtrados:
            print(personaje)
    else:
        print("No se encontraron personajes con ese nombre o letra.")


buscar_personajes()