
import itertools
import numpy as np

def getPermutation(n,d):
        
        permutations = list(itertools.permutations(range(1, n + 1)))
        permutations = sorted(permutations)
        chpermutation = np.array(list(permutations))               
        chpermutation = str(chpermutation[d-1])
        chpermutation = chpermutation.replace(" ","")
        chpermutation = chpermutation.replace("[","")
        chpermutation = chpermutation.replace("]","")
        return chpermutation  

print(getPermutation(3,3))             
    

