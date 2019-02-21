# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901

firstOfMonths = 1
count = 0
# 365 % 7 = 1 which means the first of January 1901 is a monday + one day meaning a tuesday
# thus the first sunday is on the 6th of January
sundays = 6

while year < 2001:
    if year % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28
    for month in months:
        firstOfMonths += month
        while sundays < firstOfMonths:
            sundays += 7
        if sundays == firstOfMonths:
            count += 1
    year += 1

print(count)

