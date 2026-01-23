import random

maara = int(input("Antaisitko arpakuutioiden lukumäärän?: "))

yhteensa = 0

luvut = []

for j in range(0, maara):
    luvut.append(random.randint(1,6))


for luku in luvut:
    yhteensa += luku
    
print(yhteensa)

