#!/usr/bin/python3


def print_msg(status_code, file_size):
    """Method to print
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def main():
    """Main 
    """
    import sys
    file_size = 0
    counter = 0
    status_code = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0}

    try:
        for line in sys.stdin:
            parsed_line = line.split()  # ✄ trimming
            parsed_line = parsed_line[::-1]  # inverting

            if len(parsed_line) > 2:
                counter += 1

                if counter <= 10:
                    file_size += int(parsed_line[0])  # file size
                    code = parsed_line[1]  # status code

                    if code in status_code.keys():
                        status_code[code] += 1

                if counter == 10:
                    print_msg(status_code, file_size)
                    counter = 0

    finally:
        print_msg(status_code, file_size)


if __name__ == "__main__":
    main()
