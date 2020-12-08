email = 's.gao@berkeley.edu'

def republic(cookie, ladder):
    """
    Write a function `republic` that takes in two lists.
        `cookie` is a list of strings
        `ladder` is a list of integers

    It returns a new list where every element from `cookie` is copied the
    number of times as the corresponding element in `ladder`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `cookie` and `ladder` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> republic(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> republic(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> republic(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> republic([], [1,2,3])
    []
    >>> republic(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    def republic_helper(i , outcome, ______):
        if cookie == []:
            return []
        if i <= min(len(cookie), len(ladder)) and ladder[i] >= 0:
            outcome = outcome + [cookie[i] * ladder[i]]
        else:
            cookie = cookie[: -ladder[i]]
        return republic_helper(i + 1, outcome, )
    return republic_helper(0 ,[], )

# ORIGINAL SKELETON FOLLOWS

# def republic(cookie, ladder):
#     """
#     Write a function `republic` that takes in two lists.
#         `cookie` is a list of strings
#         `ladder` is a list of integers

#     It returns a new list where every element from `cookie` is copied the
#     number of times as the corresponding element in `ladder`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `cookie` and `ladder` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> republic(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> republic(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> republic(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> republic([], [1,2,3])
#     []
#     >>> republic(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def republic_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
