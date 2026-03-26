'''
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
'''



import random

def noppa(tahkojen_maara):
    arvo = random.randint(1,tahkojen_maara)
    return(arvo)


tahkojen_maara = int(input("Antaisitko noppasi tahkojen määrä?: "))

while True:
    funktion_tulos = noppa(tahkojen_maara)
    print(funktion_tulos)
    if funktion_tulos == tahkojen_maara:
        break
