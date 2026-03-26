class ihminen:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def tervehdi(self):
        print(f"Moi olen {self.nimi}")

ihminen1 = ihminen("Pekka", 53)
ihminen1.tervehdi()