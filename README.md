# RNA_fold
# Objective function for the RNA folding problem
The problem of RNA folding is to find the native fold among the vast number of possible alignments. The native fold being the one with the lowest Gibbs free energy, the objective function must be an estimator of this energy.
**This deposit was made in the context of a [university project](https://github.com/Anthony96p/RNA_folding_problem/blob/master/TP_RNA.pdf) in a RNA bioinformatics course 
taught by <cite>_Mr. Guillaume Postic_</cite>.**
# Installation
1. Clone the repository from GitHub:
```bash
$ git clone https://github.com/Elfar-imane/RNA_fold.git
```
2. Browse to the directory where the repository was cloned:
```
cd RNA_fold
```
3. Install the necessary dependencies for the program using pip:
```
pip install -r requirements.txt
```

## Usage

### training_script1.py 

This script builds and trains an objective function using a data set of 3D RNA structures that have been determined experimentally.

```
python3 trainig_script1.py path_to_pdb_file
```

### plot_script2.py

This script produces scoring profiles, which represent the estimated Gibbs free energy as a function of interatomic distances. 

``` 
python3 plot_script2.py path_to_pdb_file
```

### score_script3.py 

This script makes use of the objective function to evaluate the accuracy of predicted structures from an RNA pdb file. 
```
python3 score_script3.py  path_to_pdb_file

```

---
## Model training

The folder `Model` contains the scripts with all functions to compute the estimated Gibb's free energy. 

### Constraints

* Only C3' atoms are taken into account
* Only "intrachain" distances are considered
* Residues must be separated by at least 3 positions on the sequence

### Observed Frequency

The probability (i.e. frequency) of observing two residues *i* and *j* separated by distance bin *r* is calculated as follows:

$$ f_{i,j} ^{OBS}(r) = { N_{i,j}(r) \over N_{i,j} } $$

where N_{i,j(r)} is the count of i and j within the distance bin r, and Ni,j is the count of i and j for
all distance bins. Only distance intervals of 0 to 20 Å are taken into account.

### Reference Frequency

The reference frequency is the same formula except that the different residue types (A, U, C, G) are indistinct ("X"):

$$ f_{X,X} ^{REF}(r) = { N_{X,X}(r) \over N_{X,X}} $$

### Pseudo-Energy

The score for each residue pair is computed as followed:

$$ u_{i,j}(r) = { -log \left( f _{i,j} ^{OBS}(r) \over f_{i,j} ^{REF}(r) \right) } $$

---

