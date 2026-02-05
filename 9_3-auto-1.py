# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0       # Alustetaan nopeus nollaksi
        self.kuljettu = 0     # Alustetaan kuljettu matka nollaksi

    # Kiihdytä-metodi
    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        # Rajoitetaan nopeus 0 ja huippunopeuden välille
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    # Kulje-metodi
    def kulje(self, tunnit):
        self.kuljettu += self.nopeus * tunnit

# Pääohjelma
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus)
print("Tämänhetkinen nopeus:", auto.nopeus)
print("Kuljettu matka:", auto.kuljettu)

# Kiihdytykset
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

# Tulostetaan nopeus
print("Nopeus kiihdysten jälkeen:", auto.nopeus)

# Hätäjarrutus
auto.kiihdytä(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus)

# Testataan kulje-metodia
auto.nopeus = 60        # Asetetaan nopeus 60 km/h
auto.kulje(1.5)         # Ajetaan 1.5 tuntia
print("Kuljettu matka 1.5 tunnin jälkeen nopeudella 60 km/h:", auto.kuljettu)
