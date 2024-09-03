#programa que usa las clases declaradas en el archivo clases
#Fecha: 02/09/2024


import clases as cl

per1 = cl.Persona("Juan",70)
per2 =cl.Persona("maria",55)
#asignar valor= asignar propiedades 
per1.peso = 75
per2.peso = 57
per2.nombre += " Elena "
#usar los metodos 
per1.caminar()
per2.comer()
per2.comer()

print("Nombre: {} y Peso: {}" ,format( per1.nombre,per1.peso))

per1.caminar(16)
print("Nombre: {} y Peso: {}" ,format( per1.nombre,per1.peso))
per1.caminar()
print("Nombre: {} y Peso: {}" ,format( per1.nombre,per1.peso))




