class Mision:
    def __init__(self, nombre, planeta_destino, nave):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = []
        self.integrantes = []

    def agregar_arma(self, arma):
        if len(self.armas) < 7:
            self.armas.append(arma)
        else:
            print("No se pueden agregar más de 7 armas.")

    def agregar_integrante(self, integrante):
        if len(self.integrantes) < 7:
            self.integrantes.append(integrante)
        else:
            print("No se pueden agregar más de 7 integrantes.")

    def __str__(self):
        return f""" ///MISIÓN///
Nombre: {self.nombre}
Planeta destino: {self.planeta_destino}
Nave: {self.nave}
Armas: {', '.join(self.armas)}
Integrantes: {', '.join(self.integrantes)}"""