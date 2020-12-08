email = 's.gao@berkeley.edu'

"""
Let a `competition` be a self-referential function that
    - takes in one integer
    - returns two values, another competition and well as an integer

For an example see the function `identity_competition` below.

You have two tasks in this assignment, to implement the functions `encyclopedia`
and `plush`. Both have their behavior defined by their doctests.

It is not necessary to implement `encyclopedia` correctly to get the points for
`plush`. However, the ok test cases for `plush` will fail if you have not correctly
implemented `encyclopedia`.
"""

def identity_competition(x):
    return identity_competition, x

def encyclopedia(a=0, s=1):
    """
    This function returns a competition function that processes a sequence
    of integers, and returns the alternating sum of all integers seen thus
    far (see doctest for an example).

    >>> competition_a = encyclopedia()
    >>> competition_b, x = competition_a(2)
    >>> x                                   # 2
    2
    >>> competition_c, x = competition_b(8)
    >>> x                                   # 2 - 8
    -6
    >>> competition_d, x = competition_c(12)
    >>> x                                   # 2 - 8 + 12
    6
    >>> competition_e, x = competition_d(30)
    >>> x                                   # 2 - 8 + 12 - 30
    -24
    >>> competition_b_again, x = competition_a(100)
    >>> x                                   # 100 [note that we are using competition_a not competition_d here]
    100
    """
    def competition(x):
        return encyclopedia(a + s * x, (-1) * s), a + s * x
    return competition

def plush(competition, items):
    """
    The function `plush` takes in a `competition` and a nonempty list of `items` and
    runs the given `competition` on each of the `items` in turn, returning the final
    numeric result.

    For example, on the items [1, 2, 3, 4, 5] with the competition encyclopedia
    we return 1 - 2 + 3 - 4 + 5 = 3

    >>> plush(encyclopedia(), [1, 2, 3, 4, 5])
    3
    >>> plush(encyclopedia(), [4000])
    4000
    >>> plush(encyclopedia(), [2, 90])
    -88
    >>> plush(identity_competition, [2, 90])
    90
    """
    competition, x = competition(items[0]), items[1:]
    if len(x) == 0:
        return items[0]
    return plush(competition, x)


# ORIGINAL SKELETON FOLLOWS

# """
# Let a `competition` be a self-referential function that
#     - takes in one integer
#     - returns two values, another competition and well as an integer

# For an example see the function `identity_competition` below.

# You have two tasks in this assignment, to implement the functions `encyclopedia`
# and `plush`. Both have their behavior defined by their doctests.

# It is not necessary to implement `encyclopedia` correctly to get the points for
# `plush`. However, the ok test cases for `plush` will fail if you have not correctly
# implemented `encyclopedia`.
# """

# def identity_competition(x):
#     return identity_competition, x

# def encyclopedia(a=0, s=1):
#     """
#     This function returns a competition function that processes a sequence
#     of integers, and returns the alternating sum of all integers seen thus
#     far (see doctest for an example).

#     >>> competition_a = encyclopedia()
#     >>> competition_b, x = competition_a(2)
#     >>> x                                   # 2
#     2
#     >>> competition_c, x = competition_b(8)
#     >>> x                                   # 2 - 8
#     -6
#     >>> competition_d, x = competition_c(12)
#     >>> x                                   # 2 - 8 + 12
#     6
#     >>> competition_e, x = competition_d(30)
#     >>> x                                   # 2 - 8 + 12 - 30
#     -24
#     >>> competition_b_again, x = competition_a(100)
#     >>> x                                   # 100 [note that we are using competition_a not competition_d here]
#     100
#     """
#     def competition(x):
#         return ______, ______
#     ______

# def plush(competition, items):
#     """
#     The function `plush` takes in a `competition` and a nonempty list of `items` and
#     runs the given `competition` on each of the `items` in turn, returning the final
#     numeric result.

#     For example, on the items [1, 2, 3, 4, 5] with the competition encyclopedia
#     we return 1 - 2 + 3 - 4 + 5 = 3

#     >>> plush(encyclopedia(), [1, 2, 3, 4, 5])
#     3
#     >>> plush(encyclopedia(), [4000])
#     4000
#     >>> plush(encyclopedia(), [2, 90])
#     -88
#     >>> plush(identity_competition, [2, 90])
#     90
#     """
#     competition, x = ______
#     if ______:
#         return ______
#     return ______

