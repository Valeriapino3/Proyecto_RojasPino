class Planeta:
    def __init__(self, nombre, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima, lista_episodios, lista_personajes):
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima
        self.lista_episodios = lista_episodios
        self.lista_personajes = lista_personajes

    def __str__(self):
        return f'-----------------Planeta-----------------\n' \
            f'Nombre: {self.nombre}\nPeriodo de orbita: {self.periodo_orbita}\nPeriodo de rotacion: {self.periodo_rotacion}\n' \
            f'Cantidad de habitantes: {self.cantidad_habitantes}\nTipo de clima: {self.tipo_clima}\nEpisodios: {self.lista_episodios}\nPersonajes: {self.lista_personajes}'