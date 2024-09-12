'''
Clase padre vehiculo, clase hija: auto
Fecha: 10/09/2024
'''
class Vehiculo:
    def __init__(self,distancia_avanzada=0):
        self.distancia_avanzada = distancia_avanzada
    def avanzar(self, velocidad=None, tiempo=None):
        if (velocidad is None and tiempo is None):
            self.distancia_avanzada += 5
        else:
            self.distancia_avanzada += (velocidad * tiempo)

class Auto(Vehiculo):
    def __init__(self, distancia_avanzada, descripcion):
        super().__init__(distancia_avanzada)
        self.descripcion = descripcion
    def retroceder(self):
        self.distancia_avanzada -= 2
    def __str__(self):
        return ('Auto (descripcion: {}, distancia_avanzada: {})'.format(self.descripcion, self.distancia_avanzada))

# Prueba
auto1 = Auto(500, "Fiat")
auto1.avanzar()
print(auto1)
auto1.avanzar(20, 2)
print(auto1)
auto1.retroceder()
auto1.retroceder()
print(auto1)








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