# Using Unsupersived Machine Learning to Predict Genetic Variation

## Running the project
This project uses a `conda` environment for all dependencies.

Instructions to recreate project:
- First, to install the dependencies, run the following command from the root directory of the project: `conda env create -f environment.yml`
- To activate the environment, run the following command: `conda activate pgv`

### Building the project stages using script.py.
This project

- To get the data, from the project root, run `python script.py data`
    - This fetches the data, creates features, cleans data and saves the data in the data directory.