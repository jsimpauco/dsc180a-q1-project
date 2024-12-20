#!/usr/bin/env python

# Imports #
import sys
import json
import src.data as data
import src.split as split
import src.kmers1 as kmers1
import src.kmers2 as kmers2
import src.all_kmers as all_kmers
import src.motif as motif
import src.maskedlm as maskedlm

# Checking if script.py is being run as a script in command line #
if __name__ == '__main__':

    # Getting args #
    args = sys.argv[1:]

    # all argument #
    if 'all' in args:

        print("\n'all' argument given. Running whole script...")

        # Setting args to all available arguments #
        args = [
            'data',
            'split',
            'kmers',
            'motif',
            'maskedlm'
        ]
    # Other arguments given #
    else:
        print('\nArguments given: ' + ', '.join(args))
        print('\nRunning script based on given arguments...')

    # data argument #
    if 'data' in args:

        print('\nCurrently running: data.py')

        # Downloading data #
        data.download_data()
    
    # split argument #
    if 'split' in args:

        print('\nCurrently running: split.py')

        # Splitting data #
        split.split_data()
    
    # kmers argument # 
    if 'kmers' in args:

        # Note: config file controls BOTH kmer1 and kmer2 python files #
        config = json.load(open('config/kmers.json'))

        print('\nCurrently running: kmers1.py')

        # Creating first half of kmers #
        kmers1.kmer_files1(**config)

        print('\nCurrently running: kmers2.py')

        # Creating second half of kmers #
        kmers2.kmer_files2(**config)

        print('\nCurrently running: all_kmers.py')

        # Concating kmers into one file #
        all_kmers.all_kmers()

    # motif argument #
    if 'motif' in args:

        config = json.load(open('config/motif.json'))

        print('\nCurrently running: motif.py')

        # Creating motif file #
        motif.motif_text(**config)

    # maskedlm argument #
    if 'maskedlm' in args:

        config = json.load(open('config/maskedlm.json'))

        print('\nCurrently running: maskedlm.py')

        # Getting results #
        maskedlm.maskedlm(**config)

    print('\nScript successfully ran!')