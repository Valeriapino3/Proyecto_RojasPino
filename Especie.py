import requests

class Especie:
    def _init_(self, nombre, altura, clasificacion, planeta_origen, lengua_materna, personajes, peliculas):
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.personajes = personajes
        self.peliculas = peliculas


    def get_nombre(self):
        return self.nombre


    def cargar_planeta(self):
        if self.planeta_origen:
            response = requests.get(self.planeta_origen)
            if response.status_code == 200:
                return response.json().get("name", "Unknown")
        return "Unknown"


    def cargar_nombres_personajes(self):
        character_names = []
        for character_url in self.personajes:
            response = requests.get(character_url)
            if response.status_code == 200:
                character_names.append(response.json().get("name", "Unknown"))
        return character_names


    def cargar_titulo_pelicula(self):
        film_titles = []
        for film_url in self.peliculas:
            response = requests.get(film_url)
            if response.status_code == 200:
                film_titles.append(response.json().get("title", "Unknown"))
        return film_titles


    def _str_(self):
        homeworld_name = self.cargar_planeta()
        character_names = self.cargar_nombres_personajes()
        film_titles = self.cargar_titulo_pelicula()
        return f""" ///ESPECIES DE STAR WARS///
Nombre: {self.nombre}
Altura: {self.altura}
Clasificación: {self.clasificacion}
Planeta de origen: {homeworld_name}
Lengua materna: {self.lengua_materna}
Personajes: {character_names}
Peliculas: {film_titles}"""