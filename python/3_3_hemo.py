

nainen_min = 117
nainen_max = 175
mies_min = 134
mies_max = 195


sukupuoli = str(input("Antaisitko sukupuolesi? (mies, nainen): ")).lower()
hemoglobiini = int(input("Antaisitko hemoglobiini arvosi?: "))

if sukupuoli == "nainen":
    if (hemoglobiini >= nainen_min) and (hemoglobiini <= nainen_max):
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi ei ole normaalilla välillä: 117-175 g/l.")
elif sukupuoli == "mies":
    if (hemoglobiini >= mies_min) and (hemoglobiini <= mies_max):
        print("Hemoglobiini arvosi on normaali")
    else:
        print("Hemoglobiini arvosi ei ole normaalilla välillä: 134-195 g/l.")
else:
    print("Virheellinen Sukupuoli")

