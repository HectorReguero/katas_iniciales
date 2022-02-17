# Ejercicio 1 
# Crearemos una variable para el usuario y la lista de planetas 
planetas = ["Mercurio", "Venus","Tierra", "Marte","Jupiter","Saturno","Neptuno","Urano", "Pluton"]
new_planet = input("Escribe el nombre de un nuevo planeta, o escribe done para salir \n")



#Comenzamons un ciclo while

while new_planet != "done":
    if new_planet:
        planetas.append(new_planet)
    new_planet = input("Escribe el nombre de un nuevo planeta, o escribe done para salir\n")

# Mostraremos los valores guardados en la lista de planetas
for x in planetas:
    print(x)