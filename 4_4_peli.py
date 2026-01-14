import random

luku = random.randint(1,10)

while True:
    kayttajan_arvaus = int(input("Antaisitko arvouksesi oikeasta luvusta (1,10): "))

    if kayttajan_arvaus == luku:
        print("Oikein")
        break
    elif kayttajan_arvaus < luku:
        print("Liian pieni arvaus")
    elif kayttajan_arvaus > luku:
        print("Liian suuri arvaus")
    else:
        print("Antaisitko kelvollisen luvun")