
class Reservation:
    seats = 10
    def SeatCap(self):  #<<seat capacity>>      
        for i in range(Reservation.seats):
            self.list1.append('0')
        print('Seat capacity:',len(self.list1),'Seats (0 = Available, 1 = Not Availabel)', '\n', self.list1)
        
    def __init__(self, list1):
        self.list1 = []
        
    def SeatAssign(self):    #>>>seat assigning<<<
        no_of_seats = int(input("Number Of Seats : "))
        if no_of_seats <= Reservation.seats:
            for i in range(Reservation.seats):
                for j in range(no_of_seats):
                    if self.list1[j] == '0':
                        self.list1[i] = '1'
            print (self.list1)
        else:
            print('Total no. of seats are', Reservation.seats)
    
res = Reservation(1)
res.SeatCap()
res.SeatAssign()

