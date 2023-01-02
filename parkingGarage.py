# Start Your Code here

class parkingGarage():
    def __init__(self):
        self.tickets = [100]
        self.parkingSpace = [100]
        self.currentTicket = {}
    
    def takeTicket(self):
        for i in range(len(self.tickets)):
            self.tickets[i] = self.tickets[i] - 1
        for i in range(len(self.parkingSpace)):
            self.parkingSpace[i] = self.parkingSpace[i] - 1

    def payForParking(self):
        self.payment = input('Please place your payment! ')
        print('Thank you for paying your ticket, you have 15mins to leave!')
        self.currentTicket2 = {'paid':True}
        self.currentTicket.update(self.currentTicket2)
       

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print('Thank You, have a nice day!')
        else:
            self.payment = input('You are trying to leave without making payment! Please place your payment. ')
            print('Thank you for paying your ticket, you have 15mins to leave!')
            self.currentTicket3 = {'paid':False}
            self.currentTicket.update(self.currentTicket3)
            print(self.currentTicket)
        for i in range(len(self.tickets)):
            self.tickets[i] = self.tickets[i] + 1
        for i in range(len(self.parkingSpace)):
            self.parkingSpace[i] = self.parkingSpace[i] + 1
        pass


parkingGarage = parkingGarage()

parkingGarage.takeTicket()
parkingGarage.payForParking()
parkingGarage.leaveGarage()

# parkingGarage.takeTicket()
# parkingGarage.leaveGarage()


# Not sure why or how the dictionary is not updating itself after you go through a happy path of the flow