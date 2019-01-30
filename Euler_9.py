# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def checkTriplet(a, b, c):
    return a*a+b*b == c*c


def product(a, b, c):
    return a+b+c == 1000


a = 0
b = 1
c = 2
true = True
while true:
    a = a + 1
    b = a + 1
    c = b + 1

    while b < c:
        c = 1000 - b - a
        if checkTriplet(a, b, c):
            print("a = {0}, b = {1}, c = {2}".format(a, b, c))
            print("product is: {0}".format(a*b*c))
            true = False
            break
        else:
            b = b+1


