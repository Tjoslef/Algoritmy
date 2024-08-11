import numpy as np
def merge_arrays(arr1, arr2):
    newarray = np.concatenate((arr1, arr2))
    newarray = np.sort(newarray)
    newarray = np.unique(newarray)
    newarray = list(newarray)
    return newarray
print(merge_arrays([1,3,5,7,9], [10,8,6,4,2]))
