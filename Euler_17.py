# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

singles = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
hundreds = 7
thousands = 8

total = 0
for i in range(1, 1000):
    single = i % 10  # singles digit
    ten = ((i % 100) - single) // 10  # tens digit
    hundred = ((i % 1000) - (ten * 10) - single) // 100  # hundreds digit

    if hundred != 0:
        total += singles[hundred] + hundreds  # "S[a] hundred
        if ten != 0 or single != 0: total += 3  # "and"
    if ten == 0 or ten == 1:
        total += singles[ten * 10 + single]
    else:
        total += tens[ten] + singles[single]

total += singles[1] + thousands
print(total)
