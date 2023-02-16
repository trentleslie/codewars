"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

https://i.imgur.com/lk5vJ7sm.jpg

Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length
a positive integer width
You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

  sqInRect(5, 3) should return [3, 2, 1, 1]
  sqInRect(3, 5) should return [3, 2, 1, 1]

"""



"""
first attempt to get my head around the problem
the trick was realizing that the final rectangle will be split into two squares,
so checking to see if the new dimenions are equal before starting the loop again
allows you to throw the last dimension into the output list

dim = [5, 3]
output = []

while dim[0] != dim[1]:

    min_dim = min(dim)
    max_dim = max(dim)

    output.append(max_dim)

    dim = [max_dim - min_dim, min_dim]

print(output)
# this output is [5, 3, 2]
"""

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    else:
        output = []
        while lng != wdth:
            min_dim = min(lng, wdth)
            max_dim = max(lng, wdth)
            output.append(min_dim)
            lng = max_dim - min_dim
            wdth = min_dim
            if lng == wdth:
                output.append(lng)
        return output
    
print(sqInRect(5, 3))

"""top codewars solution
def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res
I'm not really sure what's going on here. I think it's just a more concise way of writing the same thing
"""
