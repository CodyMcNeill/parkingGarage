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

    def payForParking(self):
        self.payment = input('Please place your payment!')
        print('Thank you for paying your ticket, you have 15mins to leave!')
        self.currentTicket2 = {'paid':True}
        self.currentTicket.update(self.currentTicket2)
       

    # def leaveGarage(self):

    
        pass


parkingGarage = parkingGarage()
print(parkingGarage.tickets)
print(parkingGarage.parkingSpace)
parkingGarage.takeTicket()
print(parkingGarage.tickets)
print(parkingGarage.parkingSpace)
print(parkingGarage.currentTicket)
parkingGarage.payForParking()

