# 4) WAP to take DOB as an input and print current age.(use inbuilt functions)

from datetime import date

class AgeCalc:
    def GetData(self): #To take input from user(name and year of birth)
        self.Name = input("Enter your name: ")
        self.Birthyear = int(input("Enter Year of Birth: "))
        self.Calc()

    def Calc(self):     # Method to calculate current age
        self.today = date.today()   # This will hold today's date.
        print("Today's Date is ", self.today)
        self.Current_age = abs(self.today.year-int(self.Birthyear)) # On subtracting birth year from current date.
        print(f"Hello {self.Name}! Your current age is {self.Current_age}")

age = AgeCalc()
age.GetData()