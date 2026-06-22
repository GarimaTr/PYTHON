class vector:
    def __init__(self,l):
        self.l=l;

    def __len__(self):
        return len(self.l)
    
    def __add__(self,v2):
        result=[a+b for a,b in zip(self.l,v2.l)]
        return result

    def __mul__(self,v2):
       result=[a*b for a,b in zip(self.l,v2.l)]
       return result 
    
    def __str__(self):
        return str(self.l)
    

a= vector([1,2,3,4])
b= vector([5,6,7,8])    
print(a+b)
print(a*b)
