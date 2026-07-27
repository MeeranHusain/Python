# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.


from random import randint 

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(meeran, fro, to):
        print(f"Ticket is booked in train no: {meeran.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self, fro, to):
        print(f"Ticket Fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        

train = Train(12399)

train.book("Mumbai", "Delhi")
train.getStatus()
train.getFare("Mumbai", "Delhi")

