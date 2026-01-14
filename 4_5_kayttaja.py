kayttaja = "python"
salasana = "rules"

for i in range(0,5):
    kayttajan_kayttaja = str(input("Käyttäjätunnus: "))
    kayttajan_salasana = str(input("Salasana: "))

    if (kayttajan_kayttaja == kayttaja) and (kayttajan_salasana == salasana):
        print("Tervetuloa")
        break


print("Pääsy evätty")