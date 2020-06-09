'''
1) Write a program that prompts the user to input number of calls 
and calculate the monthly telephone bills as per the following rule:
 Minimum Rs. 200 for up to 100 calls. Plus Rs. 0.60 per call for next 50 calls. 
 Plus Rs. 0.50 per call for next 50 calls. Plus Rs. 0.40 per call for any call beyond 200 calls.
 '''
# =====================================================================================================================


class TeleBillCalc:
    def getCall(self):      #Method to get input as number of calls from user.
        self.calls = int(input("Please Enter Number of calls:"))
        self.CalcBill()

    def CalcBill(self):     # Method to calculate the monthly bills according to question.
        if self.calls <= 100:   # If Number of calls are 100 or below.
            print("Your Monthly bill is:", 200)

        elif self.calls > 100 and self.calls <= 150:  # If Number of calls are between 101 - 150.
            self.bill = 100 + (self.calls * 0.60)
            print("Your Monthly bill is (101-150 calls):", self.bill)

        elif self.calls > 150 and self.calls <= 200: # If Number of calls are between 151 - 200.
            self.bill = 100 + (self.calls * 0.60) + (self.calls * 0.50)
            print("Your Monthly bill is (151-200 calls):", self.bill)

        else:                                   # If calls are more then 200.
            self.bill = 100 + (self.calls * 0.60) + (self.calls * 0.50) + (self.calls * 0.40)
            print("Your Monthly bill is (above 200 calls):", self.bill)
            
t = TeleBillCalc()
t.getCall()