leiviska_massa = float(8512) # 20 × 425,6 g
naula_massa = float(425.6) # 32 × 13,3 g
luoti_massa = float(13.3) #suoraan ilmoitettu grammoissa

leiviska_maara = float(input("Anna leiviskät."))
naulat_maara = float(input("Anna naulat."))
luodit_maara = float(input("Anna luodit."))

vastaus = float((leiviska_massa*leiviska_maara)+(naula_massa*naulat_maara)+(luodit_maara*luoti_massa))

kilot = int(vastaus // 1000)
grammat = float(vastaus % 1000)


print(f'{kilot} kilogrammaa')
print(f'{grammat} grammaa')
