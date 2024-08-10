class Personaje:
    def __init__(self, nombre, planeta_origen, titulos_peliculas, genero, especie, nombre_naves, nombre_vehiculos):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.titulos_peliculas = titulos_peliculas
        self.genero = genero
        self.especie = especie
        self.nombre_naves = nombre_naves
        self.nombre_vehiculos = nombre_vehiculos

    def __str__ (self):
        return f'-----------------Personaje-----------------\n' \
            f'Nombre: {self.nombre}\nPlaneta de origen: {self.planeta_origen}\nTitulos de peliculas: {self.titulos_peliculas}\n' \
            f'Genero: {self.genero}\nEspecie: {self.especie}\nNaves: {self.nombre_naves}\nVehiculos: {self.nombre_vehiculos}'