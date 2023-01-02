#!/usr/bin/python3


import re
import sys
counter = 0
file_size = 0
status_code= {200: 0, 301: 0, 400: 0,
                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_msg(status_code, file_size):
    """Method to print
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            status_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                print_msg(status_code, file_size)
            counter = counter + 1
            try:
                statusC = int(status_and_file_s.split()[0])
                f_size = int(status_and_file_s.split()[1])
                # print("Status Code {} size {}".format(statusC, f_size))
                if statusC in status_code:
                    status_code[statusC] += 1
                file_size = file_size + f_size
            except:
                pass
        print_msg(status_code, file_size)
    except KeyboardInterrupt:
        print_msg(status_code, file_size)
        raise
