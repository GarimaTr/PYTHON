def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[1,2,345,3465,7777,65,6785,4560]

f=list(filter(divisible5,a))
print(f)