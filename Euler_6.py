def sumSquareDifference():
    squaredSum = 0
    sumSquared = 0
    # range 1..100
    for i in range(1,101):
        #adding i^2 to the sum
        squaredSum += pow(i, 2)
        #adding i to the sum
        sumSquared += i
    #taking the sum and squaring it
    sumSquared = pow(sumSquared, 2)
    return abs(sumSquared-squaredSum)

print(sumSquareDifference())