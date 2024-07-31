import itertools
import numpy as np
def kInversePairs(n, k):
        permutations = list(itertools.permutations(range(n, k)))
        return permutations
print(kInversePairs(0,3))