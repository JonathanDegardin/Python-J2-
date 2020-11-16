from itertools import chain, combinations

def powerset(a):
    b = list(a)
    return chain.from_iterable(combinations(b, r) for r in range(1,len(b)+1))

a=[1,2,3,4];
b=list(powerset(a))
print(b)