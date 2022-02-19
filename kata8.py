# En esta kata 8 aprenderemos a utilizar diccionarios
# Ejercicio 1
# Primero introduciremos nuestro primer diccionario con valores 

planet = {"name":"Mars", "Moons":2}

print(planet.get("name"))
# Aqui agregamos un segundo diccionario dentro de una instancia del primer diccionario
planet ["Circunferencia(km)"] = {"polar":6752,"Equatorial":6792}
# Luego buscamos presentar solo un valor en especifico
print(planet.get("Circunferencia(km)")["polar"])


#Ejercicio 2 
# Ahora trabajaremos mas cantidad de datos en un dicicionario 
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
planets = planet_moons.keys()

print(planets)
print(moons)

print("El total de lunas es %i" %sum(moons))
print("El promedio de lunas es %f"% ((sum(moons)/len(planets))))