

kuhan_minimi_pituus = 37

kuhan_pituus = int(input("Antaisitko kuhan pituuden (cm): "))

if kuhan_pituus < kuhan_minimi_pituus:
    print("Kuhasi on alimittainen, laske se takaisin veteen")
elif kuhan_pituus >= 37:
    print("Kuhasi on iso, eikun pannulle!")
else:
    print("Virheellinen kuhan pituus, Muista laittaa pituus kokonaisina sentteinä!")