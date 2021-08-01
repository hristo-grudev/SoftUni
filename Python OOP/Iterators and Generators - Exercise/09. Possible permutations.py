import itertools


def possible_permutations(seq):
    perms = itertools.permutations(seq)
    for perm in perms:
        yield list(perm)