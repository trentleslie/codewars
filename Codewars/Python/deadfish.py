"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.
"""

def parse(data):
    
    output = [] # list to store output values
    
    # go through data string one character at a time
    for char in data:
        
        # if char is 'i', increment the value
        if char == 'i':
            value += 1
            
        # if char is 'd', decrement the value
        if char == 'd':
            value -= 1
            
        # if char is 's', square the value
        if char == 's':
            value **= 2
            
        # if char is 'o', append the value to the output list
        if char == 'o':
            output.append(value)
        
    return output

""" top codewars solution
def parse(data):
    value = 0
    res=[]
    for c in data:
        if c=="i": value+=1
        elif c=="d": value-=1
        elif c=="s": value*=value
        elif c=="o": res.append(value)
    return res
"""