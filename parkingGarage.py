# Start Your Code here

class parkingGarage():
    def __init__(self):
        self.tickets = [100]
        self.parkingSpace = [100]
        self.currentTicket = { 'paid':False }
    
    def takeTicket(self):
        for i in range(len(self.tickets)):
            self.tickets[i] = self.tickets[i] - 1
        for i in range(len(self.parkingSpace)):
            self.parkingSpace[i] = self.parkingSpace[i] - 1

    # def payForParking(self):

    # def leaveGarage(self):

    
        pass


parkingGarage = parkingGarage()
print(parkingGarage.tickets)
print(parkingGarage.parkingSpace)
parkingGarage.takeTicket()
print(parkingGarage.tickets)
print(parkingGarage.parkingSpace)

