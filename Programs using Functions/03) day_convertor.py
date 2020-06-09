'''
3)Write a program to input number of days from 
user and convert it to years, weeks and days.
Example:
Input:
Enter days: 373
Output:
373 days = 1 year/s, 1 week/s and 1 day/s
'''
# ================================================================================================================================
class DayConvertor:
    def getDay(self): # Method to take days from user.
        self.Input_days = int(input("Enter Days: "))
        self.Calc()

    def Calc(self):
        self.year = self.Input_days // 360 # Convert into years
        self.week = self.Input_days % 360 
        self.week = self.week // 7 # Convert into week
        self.day = self.week % 7  # convert into days.
        print(f"{self.Input_days} days = {self.year} year/s, {self.week} week/s and {self.day} day/s")
d = DayConvertor()
d.getDay()