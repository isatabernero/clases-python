#para ver el tipo de variable 
texto = "ejemplo"
print(type(texto))
 
anio_nacimiento = 2003
anio_actual = 2025

# recibir variable 
# declarar el método
def calcularedad(nacimiento, actual):
    edad = actual - nacimiento
    return edad 

# para llamar al método
calcularedad(anio_nacimiento, anio_actual)


print(calcularedad(anio_nacimiento, anio_actual))

#para crear nuevo método
def metodosumar():
    anio = 2024 + 1
    return anio

def anioactual():
    metodosumar()



