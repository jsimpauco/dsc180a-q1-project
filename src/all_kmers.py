#!/usr/bin/env python

"""
all_kmers.py puts the split kmer files into one file
"""

# Imports #
import gc
import os
import pandas as pd

def all_kmers():
    """
    Function that concats the two csv files
    """
    # Checks if kmers data already exists #
    if os.path.isfile('data/kmers_data/all_kmers.csv'):
        print('All kmers data already exists! Skipping creation of files')
        return
    
    print('Concatting kmers files into one file...')

    # Reading in kmer files #
    kmers1 = pd.read_csv('data/kmers_data/kmers1.csv')
    kmers2 = pd.read_csv('data/kmers_data/kmers2.csv')

    # Concating files #
    temp = pd.concat([kmers1, kmers2])

    # Freeing memory #
    del kmers1, kmers2
    gc.collect()

    # Exporting to kmers folder #
    temp.to_csv('data/kmers_data/all_kmers.csv', index=False)

    print("Creation of files complete! Data stored in 'data/kmers_data' as 'all_kmers.csv'")