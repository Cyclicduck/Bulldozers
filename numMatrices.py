import itertools as iters

# 1 if sweep, -1 if swept, 0 if neither (self = 0)
# First fill in the ones that each guy can sweep, then use symmetry to get the correct -1's.
def getMatrix(perm):
    n = len(perm)
    entries = []
    for i in range(n):
        vec = [0 for foo in range(n)]
        j = i-1
        while(j > 0 and perm[i] > perm[j]):
            vec[j] = 1
            j -= 1
  
        j = i+1
        while(j < n and perm[i] > perm[j]):
            vec[j] = 1
            j += 1

        
        entries.append(vec)
            
    # print(perm)
    for i in range(n):
        for j in range(n):
            if(entries[i][j] == 1):
                entries[j][i] = -1
                
    # print(entries)
    return tuple(tuple(blah) for blah in entries)
    
def getList(m):
    matrixList = []
    temp = [i for i in range(m)]
    for perm in iters.permutations(temp):
        matrixList.append(getMatrix(perm))
    return matrixList

def numUnique(m):
    return len(uniq(getList(m)))

# First fill in the ones that each guy can sweep, then use symmetry to get the correct -1's.
def getCycleMatrix(perm):
    n = len(perm)
    entries = []
    for i in range(n):
        vec = [0 for foo in range(n)]
        j = i-1
        while(perm[i] > perm[j%n] and (i-j)%n != 0):
            vec[j%n] = 1
            j -= 1

        j = i+1
        while(perm[i] > perm[j%n] and (i-j)%n != 0):
            vec[j%n] = 1
            j += 1        
        
        entries.append(vec)
            
    # print(perm)
    for i in range(n):
        for j in range(n):
            if(entries[i][j] == 1):
                entries[j][i] = -1
                
    # print(entries)
    return tuple(tuple(blah) for blah in entries)

def getCycleList(m):
    matrixList = []
    temp = [i for i in range(m)]
    for perm in iters.permutations(temp):
        matrixList.append(getCycleMatrix(perm))
    return matrixList

def numCycleUnique(m):
    return len(uniq(getCycleList(m)))
