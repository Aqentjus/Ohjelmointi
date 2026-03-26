'''
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
'''




import random

def noppa():
    arvo = random.randint(1,6)
    return(arvo)


while True:
    funktion_tulos = noppa()
    print(funktion_tulos)
    if funktion_tulos == 6:
        break

