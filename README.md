# Using Unsupersived Machine Learning to Predict Genetic Variation

## Running the project
This project uses a `conda` environment for all dependencies.

Instructions to recreate project:
- First, to install the dependencies, run the following command from the root directory of the project: `conda env create -f environment.yml`
- To activate the environment, run the following command: `conda activate pgv`

### Building the project stages using script.py.
This project has five total stages to build the whole project: `data`, `split`, `kmers`, `motif`, and `maskedlm`
- To run the whole project (i.e., all five stages in order), from the project root, run `python script.py all`
    - This will run the whole script with one argument.

The stages are as follows:
- To get the data, from the project root, run `python script.py data`
    - This fetches the data and saves the data in the newly created data directory.
- To split the data, from the project root, run `python script.py split`
    - This splits the data for future use when creating kmers, saving it within the data directory.
- To create the kmers data, from the project root, run `python script.py kmers`
    - This will create the kmers data and put it into split files and one large file within the data directory.
- To create the motif data, from the project root, run `python script.py motif`
    - This will create the motif data for data analysis within the motif notebook, and is tored within the data directory.
- To run the MaskedLM model, from the project root, run `python script.py maskedlm`
    - This will run the MaskedLM model on the kmers data, and store the results within the data directory.