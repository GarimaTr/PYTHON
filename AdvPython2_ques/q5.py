from functools import reduce
l=[1,2,345,3465,7777,65,6785,4560]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
    