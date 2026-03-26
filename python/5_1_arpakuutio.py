import random

maara = int(input("Antaisitko arpakuutioiden lukumäärän?: "))


for j in range(0, maara):
    print(f'Arpakuutio {j} antaa arvon {random.randint(1,6)}')