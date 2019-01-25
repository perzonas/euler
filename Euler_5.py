
# looks at the rest for all numbers between 1 and 20
# If it is 0 for all returns true, if not breaks and returns false
def testCases(number):
    for i in range(1, 21):
        if number%i != 0:
            return False
    return True


def smallestMultiple():
    current_number = 60
    while(not testCases(current_number)):
        #Only need to increase with 20 since the biggest multiple is 20
        current_number += 20
    return current_number


print(smallestMultiple())

