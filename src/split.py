#!/usr/bin/env python

"""
Splits the data for easier use when creating kmers
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
    else:
        print('dne')
    
    # Reading data #
    df = pd.read_csv('data/raw_data.csv')

    # Changing sequence to all uppercase #
    df['seq'] = df['seq'].str.upper()

    print('test complete')