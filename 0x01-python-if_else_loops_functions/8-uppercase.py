#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char

        print(upper_char, end='')

    print()
