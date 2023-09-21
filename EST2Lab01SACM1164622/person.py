class Person:
    def __init__(self,nombre,dpi,fechaNacimiento,direccion):
        self.nombre = nombre
        self.dpi = dpi
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion

    def getNombre(self):
        return self.nombre
    def getDpi(self):
        return self.dpi
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    def getDireccion(self):
        return self.direccion

    def setNombre(self,nombre):
        self.nombre = nombre
    def setDpi(self,dpi):
        self.dpi = dpi
    def setFechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    def setDireccion(self,direccion):
        self.direccion = direccion
