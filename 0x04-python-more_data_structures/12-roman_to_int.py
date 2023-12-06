#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 100
        }
    numbers = [roman_numerals[x] for x in roman_string] + [0]
    prev_value = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            prev_value += numbers[i]
        else:
            prev_value -= numbers[i]
    return (prev_value)
