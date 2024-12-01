#!/usr/bin/env python

"""
split.py splits the data for easier use when creating kmers
"""

# Imports #
import pandas as pd
import os.path

def split_data():
    """
    Splits the data into multiple files for it later to be used to create kmers.
    Also makes all the sequence strings uppercase
    """

    # Checks if data is already split #
    if os.path.isdir('data/split_data'):
        return
    
    # Reading data #
    df = pd.read_csv('data/raw_data.csv')

    # Changing sequence to all uppercase #
    df['seq'] = df['seq'].str.upper()

    # Making new folder #
    os.makedirs('data/split_data')

    # Setting variables for splitting files #
    start = 0
    end = 400000
    stopper = 2115364
    mid = 1200000
    kmers1 = 0
    kmers2 = 0

    # While loop to create files #
    while start < stopper:

        # Getting first 800,000 points #
        if end < mid:
            temp = df[start:end]
            kmers1 += 1
            temp.to_csv(f'data/split_data/kmers1_{kmers1}.csv', index=False)
            start += 400000
            end += 400000
        # Getting middle 400,000 points #
        elif end == mid:
            temp = df[start:end]
            kmers1 += 1
            temp.to_csv(f'data/split_data/kmers1_{kmers1}.csv', index=False)
            start += 400000
            end += 457682
        # Getting rest of data #
        else:
            temp = df[start:end]
            kmers2 += 1
            temp.to_csv(f'data/split_data/kmers2_{kmers2}.csv', index=False)
            start += 457682
            end += 457682