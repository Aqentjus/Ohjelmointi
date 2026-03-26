class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

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


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if hissin_numero < 0 or hissin_numero >= len(self.hissit):
            print("Virhe: hissiä ei ole olemassa!")
            return

        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("\nPALOHÄLYTYS! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"\nHissi {i} siirtyy pohjakerrokseen:")
            hissi.siirry_kerrokseen(self.alin)


# Pääohjelma
talo = Talo(1, 10, 3)

# Ajetaan hissejä eri kerroksiin
talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 3)

# Palohälytys
talo.palohalytys()