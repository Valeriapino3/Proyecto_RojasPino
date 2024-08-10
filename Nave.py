class Nave:
    def _init_(self, nombre, longitud, capacidad_carga, clasificacion_hiperimpulsor, MGLT):
        self.nombre = nombre
        self.longitud = longitud
        self.capacidad_carga = capacidad_carga
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor
        self.MGLT = MGLT

    def get_nombre(self):
        return self.nombre

    def _str_(self):
        return f"---------------------Nave---------------------\n" \
            f"Nombre: {self.nombre}\nLongitud: {self.longitud}\nCapacidad de carga: {self.capacidad_carga}\n" \
            f"Clasificacion del hiperimpulsor: {self.clasificacion_hiperimpulsor}\nMGLT: {self.MGLT}"