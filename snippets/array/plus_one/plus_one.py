"""
a) Considering all the values are 9.
b) Considering the last digit is not 9.
c) Considering the last digit is 9.
"""

def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If we're here, it means every digit was 9
    return [1] + digits

digits = [9, 9]
print(plusOne(digits))