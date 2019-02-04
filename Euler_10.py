
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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


while current_number < 2000000:
    findNextPrime()
    print(current_number)

if listOfPrimes[-1] >= 2000000:
    del listOfPrimes[-1]
print(sum(listOfPrimes))
