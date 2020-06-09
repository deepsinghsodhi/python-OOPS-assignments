'''

class Reservation:

    def __init__(self, list= None):
        if list is None:
            self.list = []


    def capacity(self):

        self.n =int(input("Enter total capacity: "))

        for i in range(self.n):
            self.list.append(0)

        while(self.n!=0):
            self.assign()
            self.n = self.n-1
           # print(self.n)


    def assign(self):

        p = int(input("Enter seat : "))
        if self.list[p-1]==0:
            self.list[p-1] =1

            print("Seat booked successfully")
        else:
            print("Seat unavailable")
        print(self.list)



r= Reservation()
r.capacity()
'''
import sys
class AirlineReservationSystem:

    def __init__(self, list = None):
        if list is None:
            self.list = []

    def assign(self):
        for i in range(1, 11):
            self.list.append(i)
        print(self.list)
        while(True):
            self.menu()

    def menu(self):
        p = int(input("\n Enter type 1 for smoking \n Enter type 2 for non smoking:"))
        if p == 1:
            self.smoking()
        if p == 2:
            self.non_smoking()
        if self.list == []:
            sys.exit("All Seats occupied")

    def smoking(self):
        q = int(input(" Enter seat: "))
        for i in range(len(self.list)):
            if (q == self.list[i] and (q > 0 and q < 6) ):
                self.list.pop(i)
                print(f" Boarding Pass-----seat no. {q} alloted in smoking section-----")
                break

            elif q not in self.list:
                if len(self.list)<=5 :
                    l = input(" Smoking section is full, Would you like to accept the seat in non smoking section ? ")
                    if (l == 'Yes'):
                        self.non_smoking()
                    elif (l == 'No'):
                        print(" Next flight leaves in three hours")
                        break

        print(self.list)

    def non_smoking(self):
        q = int(input("Enter seat: "))
        for i in range(len(self.list)):
            if (q == self.list[i] and (q > 5 and q < 11)):
                self.list.pop(i)
                print(f" Boarding Pass-----seat no. {q} alloted in non smoking section-----")
                break

            elif q not in self.list:
                if len(self.list) <= 5:
                    l = input(" Non Smoking section is full, Would you like to accept the seat in smoking section ? ")
                    if (l == 'Yes'):
                        self.smoking()
                    elif (l== 'No'):
                        print(" Next flight leaves in three hours")
                        break

        print(self.list)

   

a= AirlineReservationSystem()
a.assign()