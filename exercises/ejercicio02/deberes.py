from metodos import mostrar_info
usuarios = []  # Lista para almacenar los usuarios
seguimiento = True

while seguimiento == True:
    nombre = input("¿Que nombre tienes?")
    edad = int(input('¿Que edad tienes?'))
    correo = input("¿Cual es su correo?")
    usuario = {"nombre": nombre, "edad": edad, "correo": correo}
    mostrar_info(nombre, edad, correo)
    usuarios.append(usuario)  # Agregar usuario a la lista
    seguir = str(input("si desea añadir mas datos pulse s, en el caso que no, pulse n"))
    if(seguir== 's'):
        seguimiento = True
    else:
        seguimiento = False
        
print("\nUsuarios registrados:")
for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Correo: {usuario['correo']}")


