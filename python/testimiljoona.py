class Ihminen:
    def __init__(self, nimi, asuinkunta, tervehdys):
        self.nimi = nimi
        self.asuinkunta = asuinkunta
        self.tervehdys = tervehdys

    def tervehdi(self, tervehdys):
        print(tervehdys+ "beloo")

class Suomalainen:
    def __init__(self):
        super.__init__(self, nimi, asuinkunta, tervehdys)
        self. 




ihminen1 = Ihminen("Justus", "Helsinki", "beloo!!!")
print(ihminen1.nimi)
print(ihminen1.asuinkunta)
ihminen1.tervehdi(ihminen1.tervehdys)
