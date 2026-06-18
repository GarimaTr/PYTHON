class Employee:
    language= "Python" #This is a class attribute
    salary=1200000

    def __init__(self,name,salary,language):         #dunderMethods which is automatically called.
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")

    def getinfo(self):
        print("the language is {self.language} and salary is {self.salary}")
    @staticmethod
    def greet():
        print('good morning')

harry =Employee("harry","15000000","Javascript")

print(harry.name,harry.language,harry.salary)            