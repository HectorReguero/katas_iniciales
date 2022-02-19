# En esta kata aprenderemos a crear funciones con sus respectivos parametros
# Ejercicio 1 
# Iniciar una funcion con 3 parametros 


from ast import arguments


def combustible(t1,t2,t3):
    print("El tanque 1 esta al %i  de capacidad" % t1)
    print("El tanque 2 esta al %i  de capacidad" % t2)
    print("El tanque 3 esta al %i  de capacidad" % t3)
    print("el promedio entre los 3 tanques es %i " % promedio(t1,t2,t3))


def promedio (*args):
    r = sum(args)/len(args)
    return r


def controlMision(destino,*tiempo, **tanques):
    tanquesK =tanques.keys()
    tanquesV = tanques.values()
    
    print("Control de la mision: \nDestino: %s \nTiempo esperado: %i   " %(destino,sum(tiempo)))
    for x, y in tanques.items():
        print("Combustible en tanque %s: %i" %(x,y))




controlMision("Marte",43,54,derecha=23,izquierda=54)