# <<<<<<<<<< Company Cost of Operation Evaluation >>>>>>>>>>>>>>>.

class CostOfOperation:
    def setEmpData(self):  #This method set all the varible for operating cost.
        self.totalOperatingCost = 0 #Holds the total cost of operation.
        self.empNum = 0                #Counts for serial num of emplyee.
        self.numEmployees = int(input("Please enter the number of employees to process: ")) #Holds the num of employees to process.
        for i in range(self.numEmployees):
            self.empNum += 1
            self.empSalary = float(input(f"\nPlease enter the salary for employee {self.empNum}: ")) #Holds the salary for a single employee.
            self.fbenefits = input("Is employee 1 receiving (F)ull or (P)artial benefits? Please enter F or P: ") #ndicates if the employee is receiving full benefits.
            self.CalOperatingCost()
        print(f"your total operating cost is:","${:.2f}".format(self.totalOperatingCost))

    # Formula to calculate Total Operating Cost.
    def CalOperatingCost(self): 
        if self.fbenefits == "F" or self.fbenefits == "f": #If the employee receives full benefits
            self.totalOperatingCost += self.empSalary * 1.5
        else:
            self.totalOperatingCost += self.empSalary * 1.25


coo = CostOfOperation()
coo.setEmpData()