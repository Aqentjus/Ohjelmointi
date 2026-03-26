def listanluvut_yhteen(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa



#lukujen testausta varten 
testaus_luvut = [90, 3, 18, 19, 23, 39]
print(f'Listan lukujen summa on: {listanluvut_yhteen(testaus_luvut)}')