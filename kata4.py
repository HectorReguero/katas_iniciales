

from re import M


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

oraciones = text.split(". ")
claves = ["average","temperature","distance"]

for i in oraciones: 
    for x in claves:
        if x in i:
            r = i.replace(" C", "Celsius") 
            print(r)

name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

def plantilla(p,g,n):
    print("Datos de la gravedad en %s" %p)
    print("-"*30)
    print("Nombre del planeta: %s" %n)
    print("La gravedad de su luna es de: %f ms" %(g*1000))

plantilla(planet,gravity,name)
