from formula import calcularedad, numero_carnet 

ano_actual = 2025
def main():
    ano_nacimiento = int(input("¿Año de nacimiento?"))
    edad = calcularedad(ano_nacimiento, ano_actual)
    if (edad < 18):
        print("no puedes hacer la solicitud del carnet")
    nombre = str(input("¿Que nombre tienes?"))
    numero_DNI = int(input("cual es tu numero de DNI"))
    carnet = numero_carnet(numero_DNI)
    usuario = {"nombre": nombre, "edad": edad, "numero de carnet": carnet}
    print(usuario)
main()
 

    
