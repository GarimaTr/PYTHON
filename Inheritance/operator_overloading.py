class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,n):
        return self.n + n.n
    
n=Number(1)
m=Number(2)

print(n+m)


    