import itertools

List1=[1,2,3]

permutations = list(itertools.permutations(List1))

for permutation in permutations:
    print(permutation)
