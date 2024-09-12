"Clase empleado, nombrado y parcial"

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular(self):
        pass

class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def calcular(self):
        return self.sueldo
    
    def __str__(self):
        return 'Nombrado (Nombre: {}, Sueldo: {})'.format(self.nombre, self.calcular())

class Contratista(Empleado):
    def __init__(self, nombre, horas, tarifaPorH):
        super().__init__(nombre)
        self.horas = horas
        self.tarifaPorH = tarifaPorH
    
    def calcular(self):
        return self.horas * self.tarifaPorH
    
    def __str__(self):
        return 'Contratista (Nombre: {}, Pago por proyecto: {})'.format(self.nombre, self.calcular())

# Ejemplo de uso:
empleado1 = Nombrado('Carlos', 3000)
print(empleado1)

empleado2 = Contratista('Ana', 40, 50)
print(empleado2)








