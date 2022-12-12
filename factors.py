#!/usr/bin/python3

import sys
import resource
import time
import math

def factorize():
    start_time, start_resource = time(), getrusage(RUSAGE_)
    with open(argv[1]) as _file_:
        for _line_ in _file_:
            num = int(_line_)
            print("{:d}=".format(num), end='')
            if num % 2 == 0:
                print("{}*2".format(num//2))
                continue
