def EvenFibonacciNumbers(num):

    if num <= 1:
        return 0
    else:
        prevFibNum = 1
        FibNum = 2
        evenFibSum = 0
    
    for i in range(2, num):
        
        print("prevFibNum",prevFibNum,"FibNum:",FibNum)
        print('EvenFibNum',evenFibSum, 'num', i)
        if FibNum < num:
            if FibNum%2 == 0:
                evenFibSum += FibNum

            prevFibNum, FibNum = FibNum, prevFibNum+FibNum

    return evenFibSum


print(EvenFibonacciNumbers(100000))
