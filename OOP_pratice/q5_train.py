from random import randint
class train:

    def __init__(self,trainNo):
         self.trainNo= trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self):
         print(f"Ticket is booked in train no:{self.trainNo} running sucessfully")

    def getFare(self,fro,to):
          print(f"Ticket fair in train no:{self.trainNo} from {fro} to {to} is {randint(222,5500)}") 

t=train(12345)
t.book("Deoria","Delhi")
t.getStatus()
t.getFare("Deoria","Delhi")