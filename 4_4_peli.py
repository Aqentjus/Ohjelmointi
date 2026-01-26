import random

luku = random.randint(1,10)

while True:
    arvaus = int(input("Antaisitko arvauksesi: "))

    if arvaus == luku:
        print("Oikein")
        break
    elif arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")