#crear la clase persona y comprar datos para 2 objetos
class Persona:
    nombre = ""
    apellido = ""
    peso = 0
    
    def comer(self):
        self.peso += 1

    def caminar(self):
        self.peso-= 0.5
#realizar operaciones con clases y objetos
#crear los objetos

per1 = Persona()
per2 = Persona()
print(per1.nombre+":"+per1.apellido+ ", peso: " + str(per1.peso))
per1.nombre = " Maria"
per1,apellido = "Ramos"
per1.peso = 55

per2.nombre= "Juan"
per2.apellido="Perez"
per2.peso= 70


print(per1.nombre+ ","+ per1.apellido + ", peso:" + str(per1.peso))
print(per2.nombre+ ", " +per2.apellido + ", peso:" +str(per2.peso))
