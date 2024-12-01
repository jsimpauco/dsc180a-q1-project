#!/usr/bin/env python

"""
data.py retrieves and cleans the data required for this project
"""

# Imports #
from datasets import load_dataset
import pandas as pd
import os.path

def download_data():
    """
    Downloads the required data
    """

    # Checks if data is already downloaded #
    if os.path.isfile('data/raw_data.csv'):
        print('Raw data already exists! Skipping creation of files...')
        return

    # Loading dataset #
    ds = load_dataset("songlab/genomes-brassicales-balanced-v1")

    # Converting dataset to pandas DataFrame #
    df = ds['train'].to_pandas()

    print('Loading complete! Writing data to csv file...')

    # Making new folder if folder does not exist already #
    if not os.path.isdir('data'):
        os.makedirs('data')
    
    # Exporting to data folder #
    df.to_csv('data/raw_data.csv', index=False)

    print("Creation of files complete! Data stored in 'data' as 'raw_data.csv'")
    