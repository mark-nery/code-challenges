from itertools import *

def product(x,y):
    return x * y

def scalar(x,y):
    if len(x) == len(y):
        return reduce(lambda x,y: x + y ,list(
                map(product,x,y)))

def min_scalar_permutations(x,y):
    scalars = []
    if len(x) == len(y):
        for p in permutations(x):
            scalars.append(scalar(p,y))
    return min(scalars)
                     
def trials(s):
    return int(s.split('\n')[0])

def vectors(s):
    vectors = s.split('\n')
    del vectors[0]
    
    for i in range(0,len(vectors) - 2,2):
        del vectors[i]

    for i in vectors:
        i.split(' ')
