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

    # data argument #
    if 'data' in args:

        # Downloading data #
        data.download_data()
    
    if 'split' in args:

        # Splitting data #
        split.split_data()
    
    if 'kmers' in args:

        # Note: config file controls BOTH kmer python files #
        config = json.load(open('config/kmers.json'))

        # Creating first half of kmers #
        kmers1.kmer_files1(**config)

        # Creating second half of kmers #
        kmers2.kmer_files2(**config)

        # Concating kmers into one file #
        all_kmers.all_kmers()