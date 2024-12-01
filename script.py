#!/usr/bin/env python

# Imports #
import sys
import json
import src.data as data
import src.split as split
import src.kmers1 as kmers1
import src.kmers2 as kmers2
import src.all_kmers as all_kmers

# Checking if script.py is being run as a script in command line #
if __name__ == '__main__':

    # Getting args #
    args = sys.argv[1:]

    # all argument #
    if 'all' in args:

        print("'all' argument given. Running whole script...")

        # Setting args to all available arguments #
        args = [
            'data',
            'split',
            'kmers'
        ]

    # data argument #
    if 'data' in args:

        print('Currently running: data.py')

        # Downloading data #
        data.download_data()
    
    # split argument #
    if 'split' in args:

        print('Currently running: split.py')

        # Splitting data #
        split.split_data()
    
    # kmers argument # 
    if 'kmers' in args:

        # Note: config file controls BOTH kmer1 and kmer2 python files #
        config = json.load(open('config/kmers.json'))

        print('Currently running: kmers1.py')

        # Creating first half of kmers #
        kmers1.kmer_files1(**config)

        print('Currently running: kmers2.py')

        # Creating second half of kmers #
        kmers2.kmer_files2(**config)

        print('Currently running: all_kmers.py')

        # Concating kmers into one file #
        all_kmers.all_kmers()