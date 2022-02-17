d_Tierra = 149597870
d_Jupiter = 778547200

print("La distancia entre la tierra y jupiter es %f millas" % ((d_Jupiter-d_Tierra)*.621))

planeta1 = int(input("Dame la distancia entre el sol y el primer planeta: "))
planeta2 = int(input("Dame la distancia entre el sol y el segundo planeta: "))

print("La distancias entre ambos planetas es de %i millas" %abs(((planeta1-planeta2)*.621)))