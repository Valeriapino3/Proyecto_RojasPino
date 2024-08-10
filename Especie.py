class Especie:
    def __init__(self, nombre, altura, clasificacion, planeta_origen, lengua_materna, personajes, peliculas):
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.personajes = personajes
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} ({self.altura} cm) - {self.clasificacion} - {self.planeta_origen} - {self.lengua_materna} - {self.personajes} - {self.peliculas}"