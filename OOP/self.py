class empolyee:
    language="python"
    salary=120000

    def getinfo(self):
        print(f"langauge is {self.language} and salary is:{self.salary}")
    @staticmethod    #statcmethod let function run without object(self)
    def greet():
         print("Good morning")
harry=empolyee()
harry.language="Javascript"
# empolyee.getinfo(harry)
harry.getinfo()   
harry.greet()     