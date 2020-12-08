email = 's.gao@berkeley.edu'

def compress(file1, file2):
    """
    Write a function compress that takes in two lists of positive integers,
        file1 and file2, and determines if file1 can be compressed into file2.

    A compression is when two adjacent elements in the list are either addded or
        subtracted from each other to form one single new element.

    For example, for the list [1,2,1] the first compression could result in either

        [3, 1] (adding)
        [-1, 1] (subtraction)

    >>>> compress([1,1,1], [3])
    True
    >>>> compress([1,1,1], [2])
    False
    >>>> compress([1,1,1], [1])
    True
    >>>> compress([1,2,3], [1,5])
    True
    >>>> compress([1,2,3], [2])
    True
    >>>> compress([], [1,2,3])
    False
    >>>> compress([1,2,3], [])
    False
    >>>> compress([], [])
    True
    >>>> compress([1,4,2,8,3,9,4], [31])
    True
    >>>> compress([1,4,2,8,3,9,4], [3,5,5])
    True
    """
    if file1 == file2:
        return True
    elif file1 == [] or file2 == []:
        return False    
    compress_add = compress(([file1[0] + file1[1]] + file1[2:]), file2)
    compress_sub = compress(([file1[0] - file1[1]] + file1[2:]), file2)
    compress_eq = compress_add and compress_sub
    return compress_eq

# ORIGINAL SKELETON FOLLOWS

# def compress(file1, file2):
#     """
#     Write a function compress that takes in two lists of positive integers,
#         file1 and file2, and determines if file1 can be compressed into file2.

#     A compression is when two adjacent elements in the list are either addded or
#         subtracted from each other to form one single new element.

#     For example, for the list [1,2,1] the first compression could result in either

#         [3, 1] (adding)
#         [-1, 1] (subtraction)

#     >>>> compress([1,1,1], [3])
#     True
#     >>>> compress([1,1,1], [2])
#     False
#     >>>> compress([1,1,1], [1])
#     True
#     >>>> compress([1,2,3], [1,5])
#     True
#     >>>> compress([1,2,3], [2])
#     True
#     >>>> compress([], [1,2,3])
#     False
#     >>>> compress([1,2,3], [])
#     False
#     >>>> compress([], [])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [31])
#     True
#     >>>> compress([1,4,2,8,3,9,4], [3,5,5])
#     True
#     """
#     if ______ == ______:
#         return ______
#     elif ______ or ______:
#         return ______
#     compress_add = ______
#     compress_sub = ______
#     compress_eq = ______ and ______
#     return ______
