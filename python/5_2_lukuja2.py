'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

'''

luvut = []

while True:
    luku = input("Antaisitko luvun?: ")

    if luku is None or luku == "":
        luvut.sort(reverse=True)

        for j in range(0, 5):
            print(f'Luku {luvut[j]}')

        break
    else:
        luvut.append(int(luku))


