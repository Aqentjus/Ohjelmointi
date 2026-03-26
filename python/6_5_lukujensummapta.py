'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 

Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
'''


def luvuista_parilliset(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    
    return parilliset



testaus_luvut = [90, 3, 18, 19, 23, 39]
print(luvuista_parilliset(testaus_luvut))