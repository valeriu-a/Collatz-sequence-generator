#!/usr/bin/env python3

def collatz_sequence(x):
    if x >= 1:
        sequence = [x]
        while x != 1:
            if x % 2 == 0:
                x = int(x / 2)
                sequence.append(x)
            else:
                x = (int(x * 3) + 1)
                sequence.append(x)
        return sequence
    else:
        return []


number = int(input("Give me a positive integer: "))
print(collatz_sequence(number))
