'''
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. 
Uusi hissi on aina alimmassa kerroksessa. 
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), 
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

'''

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin  # Hissi alkaa alimmasta kerroksesta

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print("Virhe: kerros ei ole sallittu!")
            return

        while self.nykyinen_kerros < kohde:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohde:
            self.kerros_alas()


# Pääohjelma
h = Hissi(1, 10)

# Siirrytään kerrokseen 5
h.siirry_kerrokseen(5)

# Palataan alimpaan kerrokseen
h.siirry_kerrokseen(1)