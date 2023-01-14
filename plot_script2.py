import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import argparse

def PlotInteractionProfiles(scores):
    '''
    Function to plot the interaction profiles
    '''
    x = np.arange(0, 21)
    for key, value in scores.iteritems():
        plt.plot(x, value, label=key)
    plt.xlabel('Distance (Angstrom)')
    plt.ylabel('Score')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--PDB",help="inputfile",nargs='+',type = str, required = True)
    args = parser.parse_args()
    observed_freq, reference_freq, scores = obs_ref_freq_score(args.PDB)
    PlotInteractionProfiles(scores)
