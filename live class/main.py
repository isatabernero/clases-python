from datetime import datetime 
print("hello world")

# tipos de variable 
numero = 5
nombre = "Isa" 
cantidad = 5.6 
# año mes día. datetime(2025, 2, 1,)
fecha = datetime(2020,5,3)

print(numero)
print(nombre)
print(cantidad)
# print(nombre + "ha conseguido una nota de" + cantidad)

#mas variables 
tupla = (1,2,"hola") 
#siempre tienen posiciones que se le indiquen y nombre variable antes (tupla)

miarray = [1, 2, "hola"]
print(miarray)
miarray.append("adiós")
print(miarray)
# se puede añadir posiciones (lista, array)

usuario = {"nombre": "Isabel", "edad": 21}
print(usuario)
usuario["nombre"] = "raquel"
print(usuario)
#objeto. aqui dices como es: tipo de variable, su nombre y puedes acceder desde fuera. (diccionario)

# tipos de bucle 
for i in range(5):
   print(i)
# i se inicializa en 0. en este bucle se ejecuta 6 veces (0,1,2,3,4,5)

nombres = ["isabel", "maria", "raquel"]
for n in nombres:
   print (n)

u1 = {"nombre": "isabel", "edad": 21}
u2 = {"nombre": "pilar", "edad": 17}
u3 = {"nombre": "carmen", "edad": 19}

# array de objetos/diccionario
alumnos = [u1, u2, u3]

for a in alumnos:
    print(a["nombre"])
    print( a["nombre"], a["edad"])
# cuando dentro de un bucle, siempre en misma línea. Diferenciar entre bloques.

for a in alumnos:
   if a["edad"] < 18:
      print("no puede conducir")
   else:
      print("puede conducir")
      





