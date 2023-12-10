#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
              "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0

    if not roman_string:
        return (0)

    for char in roman_string:
        if char not in 'IVXLCDM':
            return (0)

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in romans:
            result += romans[roman_string[i:i+2]]
            i += 2
        else:
            result += romans[roman_string[i]]
            i += 1
    return (result)
