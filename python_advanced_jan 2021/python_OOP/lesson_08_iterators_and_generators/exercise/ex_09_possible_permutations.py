from itertools import permutations


def possible_permutations(sequence):
    result = permutations(sequence)
    for el in result:
        res = []
        for i in el:
            res.append(i)
        yield res


[print(n) for n in possible_permutations([1, 2, 3])]