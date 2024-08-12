class Pelicula:
    def _init_(self, titulo, episodio, fecha_lanzamiento, texto_inicial, director):
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.texto_inicial = texto_inicial
        self.director = director

    def get_titulo(self):
        return self.titulo

    def _str_(self):
        return f""" ///PELICULAS DE STAR WARS///
Título: {self.titulo}
Episodio: {self.episodio}
Fecha de lanzamiento: {self.fecha_lanzamiento}
Texto inicial: {self.texto_inicial}
Director: {self.director}"""