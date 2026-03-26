


gallona_litroissa = 3.785


def bensa_litroiksi(syote):
    litroina = syote / gallona_litroissa
    return litroina


while True:
    syote = float(input("Antaisitko gallonoiden määrän?: "))
    if syote <= 0:
        break
    print(bensa_litroiksi(syote))