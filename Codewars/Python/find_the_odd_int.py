"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""


def find_odd(A):
    # A is a list of integers

    #create a dictionary to store the integers and their counts
    int_dict = {}

    for i in A:
        # if i is in the dictionary, increment its value
        if i in int_dict:
            int_dict[i] += 1
        # if i is not in the dictionary, add it with a value of 1
        if i not in int_dict:
            int_dict[i] = 1
            
    # go through the dictionary and find the key with the odd value
    for key in int_dict:
        if int_dict[key] % 2 != 0:
            return key
        
print(find_odd([1,1,2,-2,5,2,4,4,-1,-2,5]))

""" top code wars solution
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
            
eliminated the need for a dictionary, just used the count method.
"""