# Vuodenajat monikkona, indeksit 0–11 vastaavat kuukausia 1–12
vuodenajat = (
    "talvi",  # tammikuu
    "talvi",  # helmikuu
    "kevät",  # maaliskuu
    "kevät",  # huhtikuu
    "kevät",  # toukokuu
    "kesä",   # kesäkuu
    "kesä",   # heinäkuu
    "kesä",   # elokuu
    "syksy",  # syyskuu
    "syksy",  # lokakuu
    "syksy",  # marraskuu
    "talvi"   # joulukuu
)

kuukausi = int(input("Anna kuukauden numero (1–12): "))

if 1 <= kuukausi <= 12:
    print("Vuodenaika on", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero")
