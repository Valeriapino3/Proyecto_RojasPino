class Vehiculo:
    def _init_(self, nombre, modelo, costo):
        self.nombre = nombre
        self.modelo = modelo
        self.costo = costo

    def get_nombre(self):
        return self.nombre

    def _str_(self):
        return f"---------------------Vehiculo---------------------\n" \
               f"Nombre: {self.nombre}\nModelo: {self.modelo}\nCosto: {self.costo}"