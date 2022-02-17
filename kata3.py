def  velocidad(x):
    if x > 25: 
        print("El cometa se mueve muy rapido")
    else:
        print("No hay problema")


def atmosfera(x):
    if x >= 20:
        print("miren todos al cielo!!")
    else:
        print("Nada que ver aqui sigan con su camino")

def peligro (dimension, velocidad):
    if dimension > 25 and velocidad > 25: 
        print ("Peligro inminente")
    elif velocidad > 20: 
        print("mira al cielo")
    elif dimension > 25: 
        print("Es posible un daño grave")
    else: 
        print("Todo tranquilo")

velocidad(63)

        