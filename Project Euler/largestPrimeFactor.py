def largestprimefactor(number):
    primeFactor = []
    for i in range (2, number):
        if number%i == 0:
            primeFactor.append(i)
    

    return primeFactor

print(largestprimefactor(10))
