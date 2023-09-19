def multiplesOf3and5(number):
    sum = 0
    for i in range (1, number) :
        if ((i % 3 == 0 ) or (i%5==0)):
            sum += int(i)
    return sum

number = int(input("Enter the Number: "))

print(multiplesOf3and5(number))