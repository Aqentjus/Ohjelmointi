luvut = []


while True:
    kayttajan_luku = input("Syöttäisitkö luvun: ")
    if kayttajan_luku is None or kayttajan_luku == "":
        luvut.sort()
        print(f'Pienin syöttämäsi luku: {luvut[0]}')
        print(f'Suurin syöttämäsi luku: {luvut[-1]}')
        break
    else:
        luvut.append(int(kayttajan_luku))


