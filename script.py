#!/usr/bin/env python

# Imports #
import sys
import src.data as data

# Checking if script.py is being run as a script in command line #
if __name__ == '__main__':

    # Getting args #
    args = sys.argv[1:]
    # print(args)

    # data argument #
    if 'data' in args:
        data.download_data()