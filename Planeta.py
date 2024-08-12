import requests

class Planeta:
    def __init__(self, nombre, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima, lista_episodios, lista_personajes):
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima
        self.lista_episodios = lista_episodios
        self.lista_personajes = lista_personajes

    def cargar_titulos_peliculas(self):
        titulos_peliculas = []
        for url_pelicula in self.lista_episodios:
            response = requests.get(url_pelicula)
            if response.status_code == 200:
                titulos_peliculas.append(response.json().get("title", "Desconocido"))
        return titulos_peliculas

    def cargar_nombres_personajes(self):
        nombres_personajes = []
        for url_personaje in self.lista_personajes:
            response = requests.get(url_personaje)
            if response.status_code == 200:
                nombres_personajes.append(response.json().get("name", "Desconocido"))
        return nombres_personajes

    def __str__(self):
        titulos_peliculas = self.cargar_titulos_peliculas()
        nombres_personajes = self.cargar_nombres_personajes()
        return f""" ///PLANETAS DE STAR WARS///
Nombre: {self.nombre}
Periodo de órbita: {self.periodo_orbita}
Periodo de rotación: {self.periodo_rotacion}
Cantidad de habitantes: {self.cantidad_habitantes}
Tipo de clima: {self.tipo_clima}
Episodios: {titulos_peliculas}
Personajes: {nombres_personajes}"""