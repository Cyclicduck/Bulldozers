import itertools as iters

# 1 if sweep, -1 if swept, 0 if neither (self = 0)
# First fill in the ones that each guy can sweep, then use symmetry to get the correct -1's.
def getMatrix(perm):
    n = len(perm)
    entries = []
    for i in range(n):
        vec = []
        j = 0
        while(j < i and perm[i] > perm[i-j-1]):
            vec.append(1)
            j += 1
        while(j <= i):
            vec.append(0)
            j += 1
  
        j = i+1
        while(j < n and perm[i] > perm[j]):
            vec.append(1)
            j += 1
        while(j < n):
            vec.append(0)
            j += 1
        
        entries.append(vec)
            
    # print(perm)
    
    for i in range(n):
        for j in range(n):
            if(entries[i][j] == 1):
                entries[j][i] = -1
    return tuple(tuple(blah) for blah in entries)
    
def getList(m):
    matrixList = []
    temp = [i for i in range(m)]
    for perm in iters.permutations(temp):
        matrixList.append(getMatrix(perm))
    return matrixList

def numUnique(m):
    return len(uniq(getList(m)))
