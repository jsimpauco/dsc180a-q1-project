"""
data_cleaning.py retrieves and cleans the data required for this project
"""

# Imports #
from datasets import load_dataset
import pandas as pd

def download_data():
    """
    Downloads the required data
    """

    # Loading dataset #
    ds = load_dataset("songlab/genomes-brassicales-balanced-v1")

    # Converting dataset to pandas DataFrame #
    df = ds['train'].to_pandas()
    
    # Exporting to data folder #
    df.to_csv('raw_data', index=False)