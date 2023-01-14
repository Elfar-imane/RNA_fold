
import numpy as np
import pandas as pd
import math
import argparse
import pickle
from training_scrip1 import file_Distances

'''the main function takes as input a pdb file and a file containing a pre-trained  model'''
def main(pdb_file, model_file):
    dist = file_Distances(pdb_file).run()
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    gibbs_free_energy = model.predict(dist)
    print('Gibbs Free Energy: ', gibbs_free_energy)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pdb_file', help="Give the path of a PdB file")
    parser.add_argument('model_file', help="Give the path to the pre-trained machine learning model file")
    args = parser.parse_args()
    main(args.pdb_file, args.model_file)


