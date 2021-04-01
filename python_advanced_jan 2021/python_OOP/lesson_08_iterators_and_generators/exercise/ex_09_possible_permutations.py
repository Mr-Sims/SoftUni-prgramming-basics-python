from itertools import permutations

# silution 1
def possible_permutations(sequence):
    result = permutations(sequence)
    for el in result:
        res = []
        for i in el:
            res.append(i)
        yield res

##solution 2
# def possible_permutations(sequence):
#     for el in permutations(sequence):
#         yield list(el)



[print(n) for n in possible_permutations([1, 2, 3])]