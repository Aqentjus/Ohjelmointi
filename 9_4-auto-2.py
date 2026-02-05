'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. 
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


'''
import random

# Auto-luokka sama kuin aiemmin
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu += self.nopeus * tunnit

# Luodaan lista auto-olioista
autot = []
for i in range(1, 11):
    huippu = random.randint(100, 200)  # Huippunopeus 100–200 km/h
    rekisteri = f"ABC-{i}"
    auto = Auto(rekisteri, huippu)
    autot.append(auto)

# Kilpailu
kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        # Arvotaan nopeuden muutos -10 ja +15 km/h
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        # Ajetaan 1 tunti
        auto.kulje(1)
    # Tarkistetaan onko joku auto ylittänyt 10000 km
    for auto in autot:
        if auto.kuljettu >= 10000:
            kilpailu_kaynnissa = False
            break

# Tulostetaan tulokset taulukoksi
print(f"{'Rekisteri':<10} {'Huippu(km/h)':<15} {'Nopeus(km/h)':<15} {'Kuljettu(km)':<15}")
print("-"*55)
for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<15} {auto.nopeus:<15} {auto.kuljettu:<15.1f}")
