'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
(ICAO-koodi on lentoaseman yksilöivä tunniste. 
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
'''



#aloitetaan 
lentokenttia = {}

def uusi_asema():
    uusi_koodi = str(input("Antaisitko uuden lentoaseman koodin ")).upper()
    uusi_nimi = str(input("Antaisitko uuden lentoaseman nimen "))
    lentokenttia[uusi_koodi] = uusi_nimi

def hae_asema():
    haettava_koodi = str(input("Antaisitko haettavan koodin?: ")).upper()
    print(f'Haetun lentoketän nimi {lentokenttia[haettava_koodi]}')




while True:
    valinta = input("Hae Asema (H), Uusi (U), Lopeta (X)> ").lower()

    if valinta == "h":
        hae_asema()
    elif valinta == "u":
        uusi_asema()
    elif valinta == "x":
        break
    else:
        print("Virheellinen valinta")