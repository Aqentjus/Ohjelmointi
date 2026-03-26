while True:
    tuuma = int(input("Antaisitko pituuden tuumissa: "))
    if tuuma < 0:
        break
    elif tuuma > 0:
        print(f'{tuuma} Tuumaa on {tuuma*2.54} Senttiä')
    else:
        pass