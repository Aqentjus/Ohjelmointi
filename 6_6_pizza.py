pi = 3.14159

def pizza_yksikkohinta(halkaisija_cm, hinta_euro):
    sade = halkaisija_cm / 2
    pinta_ala_cm2 = pi * sade ** 2
    pinta_ala_m2 = pinta_ala_cm2 / 10000
    yksikkohinta = hinta_euro / pinta_ala_m2
    return yksikkohinta


pizza_1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
pizza_1_hinta = float(input("Anna ensimmäisen pizzan hinta (€): "))

pizza_2_halkaisija = float(input("Anna toisen pizzan halkaisija (cm): "))
pizza_2_hinta = float(input("Anna toisen pizzan hinta (€): "))

yks1 = pizza_yksikkohinta(pizza_1_halkaisija, pizza_1_hinta)
yks2 = pizza_yksikkohinta(pizza_2_halkaisija, pizza_2_hinta)

if yks1 < yks2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yks2 < yks1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
    