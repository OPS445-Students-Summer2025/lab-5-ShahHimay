#!/usr/bin/env python3
# Author ID: 118541234

def read_file_string(file_name):
    # return full file content as string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # return file content as list of lines
    lines = []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines

def append_file_string(file_name, string_of_lines):
    # append given text to end of file
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    # overwrite file with each list item on new line
    with open(file_name, 'w') as f:
        for item in list_of_lines:
            f.write(str(item) + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # copy lines from one file to another with line numbers
    with open(file_name_read, 'r') as r, open(file_name_write, 'w') as w:
        for idx, line in enumerate(r, start=1):
            w.write(f"{idx}:{line.rstrip('\n')}\n")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
