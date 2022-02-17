# Ejercicio 1
# Crearemos la lista con el nombre planetas 
planetas = ["Mercurio", "Venus","Tierra", "Marte","Jupiter","Saturno","Neptuno","Urano"]

#ahora imprimimos el tamaño de la lista 
print(len(planetas))

# Ahora vamos a a gragar a pluton 
planetas.append("Pluton")
print("En el sistemasolar tenemos %i planetas, y el ultimo es %s" %(len(planetas),planetas[-1]))

# Ejercicio 2 
# Utilizaremos la misma lista de planetas 

usuario = input("Dame el nombre de un planeta, con la primera letra en mayusculas")
lugar = planetas.index(usuario)

print(" Los planetas que estan mas cerca del sol son: ",planetas[:lugar])
print(" Los planetas que estan mas lejos del sol son: ",planetas[lugar +1:])
