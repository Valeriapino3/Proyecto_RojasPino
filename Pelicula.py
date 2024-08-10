class Pelicula:
    def __init__(self, titulo, episodio, fecha_lanzamiento, texto_inicial, director):
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.texto_inicial = texto_inicial
        self.director = director

    def __str__(self):
        return f'Titulo: {self.titulo}\nEpisodio: {self.episodio}\nFecha de lanzamiento: {self.fecha_lanzamiento}\n' \
            f'Texto inicial: {self.texto_inicial}\nDirector: {self.director}'