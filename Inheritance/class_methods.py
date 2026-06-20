class Employee:
    a=1

    @classmethod    
    def show(cls):
        print(f"the class attribute of a is {cls.a}")


o=Employee()
o.a=45

o.show()
