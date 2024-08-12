import requests

class Personaje:
    def __init__(self, nombre, planeta_origen, titulos_peliculas, genero, especie, nombre_naves, nombre_vehiculos):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.titulos_peliculas = titulos_peliculas
        self.genero = genero
        self.especie = especie
        self.nombre_naves = nombre_naves
        self.nombre_vehiculos = nombre_vehiculos

    def cargar_planeta_origen(self):
        response = requests.get(self.planeta_origen)
        if response.status_code == 200:
            return response.json().get("name", "Desconocido")
        return "Desconocido"

    def cargar_titulos_peliculas(self):
        titulos_peliculas = []
        for url_pelicula in self.titulos_peliculas:
            response = requests.get(url_pelicula)
            if response.status_code == 200:
                titulos_peliculas.append(response.json().get("title", "Desconocido"))
        return titulos_peliculas

    def cargar_nombres_especies(self):
        nombres_especies = []
        for url_especie in self.especie:
            response = requests.get(url_especie)
            if response.status_code == 200:
                nombres_especies.append(response.json().get("name", "Desconocido"))
        return nombres_especies

    def cargar_nombres_naves(self):
        nombres_naves = []
        for url_nave in self.nombre_naves:
            response = requests.get(url_nave)
            if response.status_code == 200:
                nombres_naves.append(response.json().get("name", "Desconocido"))
        return nombres_naves

    def cargar_nombres_vehiculos(self):
        nombres_vehiculos = []
        for url_vehiculo in self.nombre_vehiculos:
            response = requests.get(url_vehiculo)
            if response.status_code == 200:
                nombres_vehiculos.append(response.json().get("name", "Desconocido"))
        return nombres_vehiculos

    def __str__(self):
        planeta_origen = self.cargar_planeta_origen()
        titulos_peliculas = self.cargar_titulos_peliculas()
        nombres_especies = self.cargar_nombres_especies()
        nombres_naves = self.cargar_nombres_naves()
        nombres_vehiculos = self.cargar_nombres_vehiculos()
        return f""" ///PERSONAJES DE STAR WARS///
Nombre: {self.nombre}
Planeta de origen: {planeta_origen}
Titulos de peliculas: {titulos_peliculas}
Genero: {self.genero}
Especie: {nombres_especies}
Naves: {nombres_naves}
Vehiculos: {nombres_vehiculos}"""