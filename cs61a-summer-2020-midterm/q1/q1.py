email = 's.gao@berkeley.edu'

def schedule(slideshow, sum_to, max_digit):
    """
    A 'slideshow' is a string which contains either digits or '?'s.

    A 'completion' of a slideshow is a string that is the same as slideshow, except
    with digits replacing each of the '?'s.

    Your task in this question is to find all completions of the given `slideshow`
    that use digits up to `max_digit`, and whose digits sum to `sum_to`.

    Note 1: the function int can be used to convert a string to an integer and str
        can be used to convert an integer to a string as such:

        >>> int("5")
        5
        >>> str(5)
        '5'

    Note 2: Indexing and slicing can be used on strings as well as on lists.

        >>> 'evocative'[3]
        'c'
        >>> 'evocative'[3:]
        'cative'
        >>> 'evocative'[:6]
        'evocat'
        >>> 'evocative'[3:6]
        'cat'


    >>> schedule('?????', 25, 5)
    ['55555']
    >>> schedule('???', 5, 2)
    ['122', '212', '221']
    >>> schedule('?2??11?', 5, 3)
    ['0200111', '0201110', '0210110', '1200110']
    """
    def schedule_helper(slideshow, sum_sofar, index):
        if sum(x for x in [int(slideshow)[:]]) == sum_to and ______:
            return [slideshow]
        elif len(slideshow) * max_digit < sum_to:
            return []
        elif ______:
            return schedule_helper(slideshow, sum_sofar, index + 1)
        ans = []
        for x in ______:
            modified_slideshow = ______
            ans += [modified_slideshow]
        return ans

    return schedule_helper(slideshow, 0, 0)

# ORIGINAL SKELETON FOLLOWS

# def schedule(slideshow, sum_to, max_digit):
#     """
#     A 'slideshow' is a string which contains either digits or '?'s.

#     A 'completion' of a slideshow is a string that is the same as slideshow, except
#     with digits replacing each of the '?'s.

#     Your task in this question is to find all completions of the given `slideshow`
#     that use digits up to `max_digit`, and whose digits sum to `sum_to`.

#     Note 1: the function int can be used to convert a string to an integer and str
#         can be used to convert an integer to a string as such:

#         >>> int("5")
#         5
#         >>> str(5)
#         '5'

#     Note 2: Indexing and slicing can be used on strings as well as on lists.

#         >>> 'evocative'[3]
#         'c'
#         >>> 'evocative'[3:]
#         'cative'
#         >>> 'evocative'[:6]
#         'evocat'
#         >>> 'evocative'[3:6]
#         'cat'


#     >>> schedule('?????', 25, 5)
#     ['55555']
#     >>> schedule('???', 5, 2)
#     ['122', '212', '221']
#     >>> schedule('?2??11?', 5, 3)
#     ['0200111', '0201110', '0210110', '1200110']
#     """
#     def schedule_helper(slideshow, sum_sofar, index):
#         if ______ and ______:
#             return [slideshow]
#         elif ______:
#             return []
#         elif ______:
#             return ______
#         ans = []
#         for x in ______:
#             modified_slideshow = ______
#             ______
#         return ans

#     return ______
