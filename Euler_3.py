# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math

number = 600851475143
largestFactorial = 0
tempNumber = number

step = 2
while step * step <= tempNumber:
    if tempNumber % step == 0:
        tempNumber = tempNumber/step
        largestFactorial = step
    else:
        if step % 2 == 0:
            step += 1
        else:
            step += 2
if tempNumber > largestFactorial:
    largestFactorial = tempNumber
print(largestFactorial)