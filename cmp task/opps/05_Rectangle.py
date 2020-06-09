'''
5)   Create a class named 'Rectangle' with two data members 'length' and
 'breadth' and two methods to print the area and perimeter of the rectangle 
 respectively. Its constructor having parameters for length and breadth is 
 used to initialize length and breadth of the rectangle. Let class 'Square' 
 inherit the 'Rectangle' class with its constructor having a parameter for
  its side (suppose s) calling the constructor of its parent class using 'super()'.
   Print the area and perimeter of a rectangle and a square.
'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def Area(self):
        arRec = self.length * self.breadth
        arSq = self.side * self.side
        print('Area of Rectangle is:', arRec)
        print('Area of Square is:', arSq)

    def Perimeter(self):
        periRec = 2 * (self.length + self.breadth)
        periSq = 4 * self.side
        print("\nPerimeter of Rectangle is:", periRec)
        print("Perimeter of Square is:", periSq)

class Square(Rectangle):
    def __init__(self, side, length, breadth):
        self.side = side
        self.length = length
        self.breadth = breadth
        super().__init__(self.length, self.breadth)
        
s = Square(5, 20, 40)
s.Area()
s.Perimeter()

