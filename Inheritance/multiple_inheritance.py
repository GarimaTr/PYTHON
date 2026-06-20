class Employee:
    company="ITC"
    name="Shubham"
    salary=120000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all the language,your language is: {self.language}")


class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showLanguage(self):
     print(f"The name is {self.company} and he is good with {self.language} language")  

a=Employee()
b=Programmer()

b.show()
b.showLanguage()
b.printLanguage()
