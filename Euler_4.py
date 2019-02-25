
# reverses a string
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


# compares the reversed and the normal string to see if it is a palindrome
def isPalindrome(number):
    return str(number) == reverse(str(number))


def largestPalindromeProduct():
    second = 999
    first = 999
    largestPalindrome = 0
    while(first > 100):
        while( second > 100):
            calculatedValue = first*second
            #if the multiple is smaller then the largest palindrome there is no point
            # in continuing the outer loop
            if calculatedValue < largestPalindrome:
                break

            # Looks if the new value is a palindrome and then sets
            # the new value to the largest palindrome
            if isPalindrome(calculatedValue):
                largestPalindrome = calculatedValue
            second -= 1
        # resets the outer loop
        second = 999
        first -= 1

    # prints the answer
    print(largestPalindrome)


largestPalindromeProduct()