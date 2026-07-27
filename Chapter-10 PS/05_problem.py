# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint 

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self, fro, to):
        print(f"Ticket Fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        

train = Train(12399)

train.book("Mumbai", "Delhi")
train.getStatus()
train.getFare("Mumbai", "Delhi")

