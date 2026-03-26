nimet = set()

while True:
    kayttajan_syote = str(input("Syöttäisitkö nimen joka lisätään: "))

    if kayttajan_syote == len(0):
        break
    else:
        if kayttajan_syote in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(kayttajan_syote)