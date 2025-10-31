#!/usr/bin/env python3
# Author ID: 118541234

def read_file_string(file_name):
    # open file and return all text as one string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # open file and return list of lines without newlines
    lines = []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
