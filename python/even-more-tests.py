def high_and_low(numbers):
    numberr = []
    for number in numbers:
        if number != " ":
            numberr.append(number)
        else:
            pass
    numberr.sort()
    numbers = f"{numberr[0]} {numberr[-1]}"
    return numbers


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
