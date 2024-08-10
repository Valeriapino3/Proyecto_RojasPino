import requests
from Especies import Especies
from Pelicula import Pelicula


BASEURL = "https://www.swapi.tech/api/"

def fetch_data(endpoint):
    response = requests.get(f"{BASEURL}{endpoint}")
    if response.status_code == 200:
        return response.json()["result"]
    return None

def get_films():
    films_data = fetch_data("films")
    films = []
    for film_data in films_data:
        properties = film_data["properties"]
        film = Pelicula(properties["title"], properties["episode_id"],properties['release_date'], properties["opening_crawl"], properties["director"])
        films.append(film)
    return films