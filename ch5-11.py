# Ryan Zmuda
# SOFT 204 Open Source Programming
# 5-11 Ordinal Numbers

print("#5-11 Ordinal Numbers\n")

digits = [value for value in range(1, 11)]
for digit in digits:
    if digit == 1:
        print(str(digit) + "st")
    elif digit == 2:
        print(str(digit) + "nd")
    elif digit == 3:
        print(str(digit) + "rd")
    else:
        print(str(digit) + "th")
