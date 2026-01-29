import random

flag = True

def noppa():
    arvo = random.randint(1,6)
    return(arvo)


while flag:
    funktion_tulos = noppa()
    print(funktion_tulos)
    if funktion_tulos == 6:
        flag = False



