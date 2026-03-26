class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko



sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)


sahkoauto.nopeus = 120
polttomoottoriauto.nopeus = 100


sahkoauto.aja(3)
polttomoottoriauto.aja(3)


print(f"Sähköauto {sahkoauto.rekisteritunnus}, matka: {sahkoauto.matkamittari} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus}, matka: {polttomoottoriauto.matkamittari} km")