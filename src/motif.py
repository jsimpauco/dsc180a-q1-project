#!/usr/bin/env python

"""
motif.py creates a motif.txt file to create the plots generated in motif.ipynb notebook
"""

# Imports #
import os
import pandas as pd
from collections import Counter

def generate_18mers(kmer_string):
    """
    Function to generate 18-character motifs

    kmer_string (str): Given kmer string

    Returns an 18 character motif
    """
    # Split each string into individual short k-mers #
    short_kmers = kmer_string.split()

    # Concatenate every 3 consecutive 6-mers to form 18-character motifs #
    return ["".join(short_kmers[i:i+3]) for i in range(len(short_kmers) - 2)]

def motif_text(chunksize):
    """
    Creates a motif.txt file for later use

    chunksize (int): Define chunksize to manage memory usage, adjust based on available memory

    Saves a file within the data/ directory
    """
    # Checks if motif data already exists #
    if os.path.isfile('data/motifs.txt'):
        print('Motif data already exists! Skipping creation of files...')
        return
    
    # Check if all_kmers.csv exists (needed to run function) #
    if not os.path.isfile('data/kmers_data/all_kmers.csv'):
        print("all_kmers.csv needed to get motif files! Please run the 'kmers' argument before proceeding")
        return
    
    # Initialize the Counter #
    kmer_counts = Counter()

    # Process the file in chunks to manage memory usage #
    for chunk in pd.read_csv('data/kmers_data/all_kmers.csv', chunksize=chunksize):
        for kmer_string in chunk['kmer_string']:

            # Generate 18-character motifs from the current kmer_string #
            motifs_18 = generate_18mers(kmer_string)
            
            # Update the global Counter with the 18-character motifs #
            kmer_counts.update(motifs_18)

    # Get the most common 18-character motifs (top 50 motifs) #
    top_kmers = kmer_counts.most_common(50)

    # Save the top 50 motifs to a text file for WebLogo #
    with open('data/motifs.txt', 'w') as f:
        for kmer, count in top_kmers:
            f.write(f'{kmer}: {count}\n')

    print("Creation of files complete! Data stored in 'data/' as 'motifs.txt'")