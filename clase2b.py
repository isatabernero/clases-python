#entiende metodos porq esta en la misma carpeta
#te importa solo lo que necesitas de esa libreria: cn , te importa añades otro
from metodos import raiz_cuadrada, random

#metodo principal dnd se ejecuta todo
def main():
    #pedir un  umero en pantalla
    numero = int(input('Ingrese número?'))
    y = raiz_cuadrada(numero)
    print("La raíz es: ", y)
    x = random()
    print(x)
main()

#hacer main llamando a metodos y crear algun metodo que imprima frase, pregunte por nombre. print luego
# otro en que año naciste y que te devuelva que edad tienes. 