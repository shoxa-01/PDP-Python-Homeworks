Depozit = 100
Foiz = 0.01
Foyda = 200


x = 0
som = Depozit

while som < Foyda:
    som *= (1 + Foiz)
    x += 1


print(x)
