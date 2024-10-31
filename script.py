#!/usr/bin/env python

# Imports #
import sys
import json
import src.data as data

# Checking if script.py is being run as a script in command line #
if __name__ == '__main__':

    # Getting args #
    args = sys.argv[1:]

    # data argument #
    if 'data' in args:

        # downloading data #
        data.download_data()

        # cleaning data #
        config = json.load(open('config/data.json'))
        data.clean_data(**config)