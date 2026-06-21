class Animals:
    pass

class Pets(Animals):
    pass

class dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!!!")

d=dog()
d.bark()        