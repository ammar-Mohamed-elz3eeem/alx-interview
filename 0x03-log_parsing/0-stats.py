#!/usr/bin/python3
"""Make script that log the request send to it
"""
import sys


def signal_handler(d, total_file_size):
    """Generate message when signal detected"""
    print("File size: {}".format(total_file_size))
    for key, val in sorted(d.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
try:
    parsed_line = []
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]
        if len(parsed_line) > 2:
            counter += 1
            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]
                if code in codes:
                    codes[code] += 1
            if counter == 10:
                signal_handler(codes, total_file_size)
                counter = 0
finally:
    signal_handler(codes, total_file_size)
