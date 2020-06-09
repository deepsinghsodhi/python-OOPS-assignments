'''
2) A small company dealing with transportation has just purchased a computer for its new automated reservations system. 
    You have been asked to program the new system. You are to write a program called ReservationSystem  to assign seats on a vehicle. 
    Your class also requires the following:·   
  1.   a constructor , which initialize the LIST· Use a LIST  to represent the seating chart of the plane
  2.   a method to assign the capacity of seating.·   
  3.   a method for assigning seats. 
'''


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

