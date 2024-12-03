#!/usr/bin/env python

"""
model.py
"""

# Imports #
import gc
import torch
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModelForMaskedLM

def tokenize(kmers):
    """
    Tokenize using DNABERT tokenizer.
    """
    # Put kmers into list #
    kmers = kmers.split()

    # Tokenize kmers #
    return tokenizer(" ".join(kmers), return_tensors="pt")

def process_sequence(batch_size):
    """
    erm what the sigma
    """
    print(batch_size)
    # Load the pre-trained DNA model and tokenizer #
    model_name = "zhihan1996/DNA_bert_6"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)
    return