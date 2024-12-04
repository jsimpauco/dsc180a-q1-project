#!/usr/bin/env python

"""
maskedlm.py runs a MaskedLM model on kmers data
"""

# Imports #
import os
import gc
import torch
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForMaskedLM

def tokenize(kmers, tokenizer):
    """
    Tokenize using DNABERT tokenizer
    """
    # Put kmers into list #
    kmers = kmers.split()

    # Tokenize kmers #
    return tokenizer(" ".join(kmers), return_tensors="pt")

def maskedlm(batch_size, percentage):
    """
    Runs a MaskedLM model on kmers data, storing results within the data folder
    """
    # Checks if MaskedML results data already exists #
    if os.path.isfile('data/results.npy'):
        print('MaskedML results already exists! Skipping creation of files...')
        return

    # Check if all_kmers.csv exists (needed to run function) #
    if not os.path.isfile('data/kmers_data/all_kmers.csv'):
        print("all_kmers.csv needed to get maskedlm files! Please run the 'kmers' argument before proceeding")
        return

    # Loading in dataset #
    df = pd.read_csv('data/kmers_data/all_kmers.csv')

    # Getting percentage of dataset based on input #
    base_length = df.shape[0]
    total_length = int(np.floor(percentage * base_length))
    df = df.head(total_length)

    # Load the pre-trained DNA model and tokenizer #
    model_name = "zhihan1996/DNA_bert_6"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)

    # Setting variables #
    seq_len = 509
    vocab_size = 4101
    output_shape = (total_length, seq_len, vocab_size)
    dtype = np.float32

    # Memory-mapped file to store the results and save on memory usage #
    memmap_results = np.memmap('data/results.npy', dtype=dtype, mode='w+', shape=output_shape)

    # Looping through batches #
    for start in range(0, total_length, batch_size):

        # Select the batch #
        batch_df = df.iloc[start:start + batch_size]

        # Tokenize sequences #
        tokenized_sequences = [
            tokenize(kmer, tokenizer)['input_ids'] for kmer in batch_df['kmer_string']
        ]
        # Combine tokenized inputs into a tensor #
        tokenized_batch = torch.cat(tokenized_sequences, dim=0)

        # Send inputs to the model #
        with torch.no_grad():
            outputs = model(input_ids=tokenized_batch)

        # Extract logits (or probabilities if needed) #
        logits = outputs.logits

        # Process the logits (optional: convert to probabilities or extract specific scores) #
        probabilities = torch.softmax(logits, dim=-1).numpy()

        # Store the results directly in the memory-mapped file #
        memmap_results[start:start + batch_size] = probabilities

        # Free memory #
        del tokenized_batch, outputs, probabilities
        gc.collect()

        print(f"Processed batch {start // batch_size + 1} of {total_length // batch_size + 1}")

    # Ensuring that the file is properly written and closed #
    del memmap_results
    gc.collect()
    
    print("Creation of files complete! Data stored in 'data/' as 'results.npy'")