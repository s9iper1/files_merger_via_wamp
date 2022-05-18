# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_file(file_name):
    with open(file_name) as f:
        return f.readlines()


def writing_single_file(file_1_data, file_2_data, file_3_data):
    with open('result/result.txt', 'w+') as f:
        f.writelines(file_1_data)
        f.writelines(file_2_data)
        f.writelines(file_3_data)


if __name__ == '__main__':
    file_1_lines = read_file('file1.txt')
    file_2_lines = read_file('file2.txt')
    file_3_lines = read_file('file3.txt')
    writing_single_file(file_1_lines, file_2_lines, file_3_lines)
