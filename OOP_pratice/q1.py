class programmer:
    company="microsoft"
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age

p=programmer("Harry","120000","23")        
print(p.name,p.salary,p.age)
q=programmer("Dashi","157000","25")        
print(q.name,q.salary,q.age)