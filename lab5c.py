#!/usr/bin/env python3
# Author ID: 118541234

def add(number1, number2):
    # try adding numbers, return error string if invalid
    try:
        a = int(number1)
        b = int(number2)
        return a + b
    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    # try reading a file, return error string if fails
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except OSError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
