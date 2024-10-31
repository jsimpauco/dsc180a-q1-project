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
        return

    # Loading dataset #
    ds = load_dataset("songlab/genomes-brassicales-balanced-v1")

    # Converting dataset to pandas DataFrame #
    df = ds['train'].to_pandas()
    
    # Exporting to data folder #
    df.to_csv('data/raw_data.csv', index=False)