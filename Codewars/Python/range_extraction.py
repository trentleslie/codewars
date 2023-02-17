
"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
# """

# this is ugly and doesn't work for all random test cases, but it passes all the tests

def solution(args):

    args = sorted(args)
    range_str = ''

    for i in range(len(args)):
        
        if len(args) == i + 2:
            range_str += "," + str(args[i]) + ',' + str(args[i + 1])
        
        if len(args) > i + 3:
            if args[i] + 1 == args[i + 1] and args[i] + 2 == args[i + 2]:
                max_range = args[i + 2]
                
                j = i + 3
                seq_add = 3
                
                while j in range(len(args)):
                    if args[i] + seq_add == args[j]:
                        max_range = args[j]
                        j += 1
                        seq_add += 1
                    else:
                        break
                    
                if i == 0:
                    range_str = str(args[i]) + '-' + str(max_range)
                else:
                    range_str += "," + str(args[i]) + '-' + str(max_range)
                
                for k in range(j - i - 1):
                    args.pop(i + 1)

            else:
                if i == 0:
                    range_str = str(args[i])
                else:
                    range_str += "," + str(args[i])
        
  
                
        if i == len(args) - 1:
            break

    return range_str

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
            
"""top codewars solution

# i don't really understand this one, but it's cool

def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)

# this is how chatgpt explains it

This function is a solution for a specific problem that involves formatting a list of integers as a comma-separated string, where consecutive integers are grouped together using ranges. Here's how the function works:

The input list of integers args is initialized, and two variables beg and end are set to the first element of the list. out is also initialized as an empty list to store the output string.

The function iterates over the remaining elements of args (i.e., args[1:]) plus a dummy empty string "" at the end. This is done to handle the last range in the list.

For each element n in the iteration, the function checks whether it is consecutive to the previous element end using the expression n != end + 1. If it is, then the range continues; otherwise, a new range begins.

If the range has only one element (i.e., beg == end), the function appends a string representation of beg to out.

If the range has two elements (i.e., end == beg + 1), the function extends out with two string representations of beg and end.

If the range has more than two elements, the function appends a string representation of beg concatenated with a hyphen - and a string representation of end to out.

Finally, the function joins the elements of out into a comma-separated string using the join method and returns the result.

In summary, this function takes a list of integers and groups consecutive integers into ranges, and then formats the result as a comma-separated string. For example, if the input list is [1, 2, 3, 5, 6, 7, 9, 10], the function will return the string "1-3,5-7,9-10".

"""
