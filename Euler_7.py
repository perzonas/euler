# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


listOfPrimes = [2]
current_number = 1


# Looks if a given number is a prime number by comparing it to the
# list of primes found already
def isPrime(number):
    global listOfPrimes
    for prime in listOfPrimes:
        if number % prime == 0:
            return False
    return True


# Finds the next prime number in succession
def findNextPrime():
    global current_number
    global listOfPrimes
    while True:
        current_number = current_number + 2
        if isPrime(current_number):
            listOfPrimes.append(current_number)
            break


# Finds number of primes given to the function
def findAllPrimes(number):
    global current_number
    global listOfPrimes

    while len(listOfPrimes) < number:
        findNextPrime()


# finds the first 10001 prime numbers
findAllPrimes(10001)
print(current_number)

