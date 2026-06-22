class vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,v2):
        return vector(self.x+ v2.x,self.y+v2.y,self.z+v2.z)
    
    def __mul__(self,v2):
        result= self.x*v2.x + self.y*v2.y + self.z*v2.z
        return result
    
    def __str__(self):
        return f"{self.x}x +{self.y}y + {self.z}z"

a=vector(1,2,3)
b=vector(4,5,6)
print(a+b)
print(a*b)