#!/usr/bin/env python

"""
Makes first half of kmer files for use later
"""

# Imports #
import gc
import os
import pandas as pd
import warnings # Prevents popups of any possible warnings #
warnings.filterwarnings('ignore')

def preprocess_sequence(sequence, strand):
    """
    Function to preprocess sequence and handle strand
    Convert sequence to uppercase and reverse-complement if strand is '-'
    """
    sequence = sequence.upper()
    if strand == "-":
        complement = str.maketrans("ATCG", "TAGC")
        sequence = sequence.translate(complement)[::-1]
    return sequence

def generate_kmers(sequence, k):
    """
    Function to generate overlapping k-mers from a sequence
    Generate overlapping k-mers of length k
    """
    # Yielding k-mers one at a time to avoid creating large lists in memory #
    for i in range(len(sequence) - k + 1):
        yield sequence[i:i + k]

def process_batch(batch_df, k):
    """
    Preprocess and generate k-mers for each row in a batch DataFrame
    """
    all_kmers = []
    for _, row in batch_df.iterrows():
        # Preprocess the sequence and generate k-mers #
        sequence = preprocess_sequence(row['seq'], row['strand'])
        kmers = generate_kmers(sequence, k)  # Generator, not list #
        all_kmers.append(" ".join(kmers))
    
    # Return the k-mer strings for the batch #
    return all_kmers

def kmer_files1(batch_size, k):
    """
    Create the needed kmer files

    batch_size: Define batch size to manage memory usage, adjust based on available memory
    k: Size of generated k-mers at length k
    """
    # Checks if kmers data already exists #
    if os.path.isfile('data/kmers_data/kmers1.csv'):
        print('1st half of kmers data already exists! Skipping creation of files')
        return
    
    # Initialize an empty list to store k-mer strings
    all_kmers = []

    # Getting 1st half of kmers #
    print('Creating 1st half of kmers:')
    for i in range(1,4):
        print(f'Currently on iteration {i}/3...')
        df = pd.read_csv(f'data/split_data/kmers1_{i}.csv')

        # Process the DataFrame in batches to avoid memory overload
        for start in range(0, len(df), batch_size):
            # Select the current batch
            curr_batch_df = df.iloc[start:start + batch_size]
            
            # Process the batch to generate k-mer strings
            processed_batch = process_batch(curr_batch_df, k)
            
            # Append the k-mer strings from the batch to the results list
            all_kmers.extend(processed_batch)
            
            # Clear memory for the processed batch
            del curr_batch_df, processed_batch
            gc.collect()

    # Convert the list of k-mer strings to a DataFrame
    df_kmers = pd.DataFrame(all_kmers, columns=['kmer_string'])

    print('Iterations complete! Writing data to csv file...')

    # Making new folder if folder does not exist already #
    if not os.path.isdir('data/kmers_data'):
        os.makedirs('data/kmers_data')

    # Exporting to kmers folder #
    df_kmers.to_csv('data/kmers_data/kmers1.csv', index=False)

    print("Creation of files complete! Data stored in 'data/kmers_data' as 'kmers1.csv'")