class DoorPuzzle:
    def SetDoor(self): # This method multiple the door hunderd times
        self.doors = [0]*100
        # print("Initially closed doors: ", self.doors)
        self.CaclDoor()

    def CaclDoor(self): #This method will toggle the doors.
        for x in range (1, 101):
            for y in range (x-1, 100, x):
                if self.doors[y] == 0:
                    self.doors[y] = 1
                elif self.doors[y] == 1:
                    self.doors[y] = 0
                else:
                    pass
        self.OpenDoors()

    def OpenDoors(self): # This method calculate the number of open doors.
        self.opendoors = []   # This list will hold the open doors.
        for i, self.value in enumerate(self.doors):
            if self.value == 1:
                self.opendoors.append(i+1)
            else:
                pass
        print('Numbers of open:', self.opendoors)
        self.ClosedDoors()

    def ClosedDoors(self): # This method calculate the number of Closed doors.
        self.closedoors = []
        for i in range(1, 101):
            if i not in self.opendoors:
                self.closedoors.append(i)
            else:
                pass
        print("Closed doors are: ", self.closedoors)

d = DoorPuzzle()
d.SetDoor()