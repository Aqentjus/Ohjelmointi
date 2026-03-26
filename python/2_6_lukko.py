import random

kolme_koodi = ""
neli_koodi = ""

for i in range (0,3):
    kolme_koodi += str(random.randint(0,9))

for i in range (0,4):
    neli_koodi += str(random.randint(1,6))

print(f'Kolminumeroinen satunnainen koodisi on: {kolme_koodi}')
print(f'Nelinumeroinen satunnainen koodisi on: {neli_koodi}')