class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0


# Pääohjelma
auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto.tamanhetkinen_nopeus, "km/h")
print("Kuljettu matka:", auto.kuljettu_matka, "km")
