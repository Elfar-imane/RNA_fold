import numpy as np
import pandas as pd
import math
import argparse

def atom_dist(x,y,z):
    """the distance between two atoms in the sequence """ 
    d= math.sqrt([x+y+z])
return(d)


def read_pdb(file):
    all_lines = []   
    for f in files:
        with open(f,'r') as ff:
            for line in ff:
                if line.startswith("ATOM"):
                    all_lines.append(line)
    return all_lines
def file_Distances(file):
    lines_list = read_pdb(files)
    distance = {}
    AA,AU,AC,AG,UU,UG,UC,CC,CG,GG = [],[],[],[],[],[],[],[],[],[]
    i = 0
    while i < len(lines_list):
        j = i
        while j < len(lines_list):
            if abs(float(lines_list[i][22:26].strip())-float(lines_list[j][22:26].strip())) >=4:
                if lines_list[i][13:16].strip() == "C3'":
                    if lines_list[j][13:16].strip() == "C3'":
                        pair = lines_list[i][18:20].strip()+lines_list[j][18:20].strip()
                        x = (float(lines_list[i][31:38].strip()) -  float(lines_list[j][31:38].strip()))**2
                        y = (float(lines_list[i][39:46].strip()) - float(lines_list[j][39:46].strip()))**2
                        z=(float(lines_list[i][47:54].strip())-float(lines_list[j][47:54].strip()))**2
                        d = atom_dist(x+y+z)
                        if d<21:
                            if pair == "AA":
                                AA.append(d)
                            if pair == "AU" or pair == "UA" :
                                AU.append(d)
                            if pair == "AC" or pair == "CA":
                                AC.append(d)
                            if pair == "AG" or pair == "AG":
                                AG.append(d)
                            if pair == "UU":
                                UU.append(d)
                            if pair == "UG" or pair == "GU":
                                UG.append(d)
                            if pair == "UC" or pair == "CU":
                                UC.append(d)
                            if pair == "CC":
                                CC.append(d)
                            if pair == "CG" or pair == "GC":
                                CG.append(d)
                            if pair == "GG":
                                GG.append(d)
    distance["AA"]=AA
    distance["AU"]=AU
    distance["AC"]=AC
    distance["AG"]=AG
    distance["UU"]=UU
    distance["UG"]=UG
    distance["UC"]=UC
    distance["CC"]=CC
    distance["CG"]=CG
    distance["GG"]=GG
    print(distance)
    return distance 



def obs_ref_freq_score(pdb_file):
    
    distances = file_Distances(pdb_file)
    observed_freq = pd.DataFrame(index=np.arange(0, 21))
    reference_freq = pd.DataFrame(index=np.arange(0, 21))
    scores = pd.DataFrame(index=distances.keys())
    for key, value in distances.items():
        observed_freq[key] = np.histogram(value, bins=np.arange(0, 21, 1))[0]
        reference_freq[key] = np.random.poisson(lam=np.mean(value), size=20)
        scores[key] = sum((observed_freq[key] - reference_freq[key]) ** 2)
    return observed_freq, reference_freq, scores



   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--PDB",help="pdbfile",nargs='+',type = str, required = True)
    args = parser.parse_args()
    observed_freq, reference_freq, scores = obs_ref_freq_score(args.PDB)
    print(observed_freq)
    print(reference_freq)
    print(scores)
