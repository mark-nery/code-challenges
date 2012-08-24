from itertools import *

def product(x,y):
    return x * y

def scalar(x,y):
    if len(x) == len(y):
        return reduce(lambda x,y: x + y ,list(
                map(product,x,y)))

#was too slow for large test
def min_scalar_permutations(vector_pair):
    x = vector_pair[0]
    y = vector_pair[1]
    scalars = []
    if len(x) == len(y):
        for p in permutations(x):
            scalars.append(scalar(p,y))
    return min(scalars)

def min_scalar_ordering(vector_pair):
    return scalar(sorted(vector_pair[0]) ,sorted(vector_pair[1],reverse = True))

def trials(s):
    return int(s.split('\n')[0])

def get_vectors(s):
    vectors = s.split('\n')
    return zip(
        map(lambda x: map(int,x.split(' ')),vectors[2::3]), 
        map(lambda x: map(int,x.split(' ')),vectors[3::3]))
