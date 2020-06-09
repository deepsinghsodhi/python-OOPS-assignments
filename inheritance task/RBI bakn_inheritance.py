'''
All the banks operating in India are controlled by RBI. RBI has set a well defined guideline 
(e.g. minimum interest rate, minimum balance allowed, maximum withdrawal limit etc) 
which all banks must follow. For example, suppose RBI has set minimum interest rate 
applicable to a saving bank account to be 4% annually; however, banks are free to use 
4% interest rate or to set any rates above it.

Write a program to implement bank functionality in the above scenario and demonstrate 
the dynamic polymorphism concept. Note: Create few classes namely Customer, Account, 
RBI (Base Class) and few derived classes (SBI, ICICI, PNB etc).

Assume and implement required instance variables and methods in each class.
'''

class RBI:                                                 #<<<< RBI >>>>>
    def __init__(self, min_bal = 5000 , min_rate = 4, max_wdr = 50000 ):
        self.min_bal  = min_bal
        self.min_rate = min_rate
        self.max_wdr  = max_wdr
        print("init by RBI class by super")

    def getRBI(self):
        print("*************RBI Rules*************")
        print("Minimum Balance allowed:", self.min_bal)
        print("Minimum Rate of Intrest:", self.min_rate)
        print("Maximum Withdrawl Limit:", self.max_wdr)
  
class Account:
    def __init__(self):
        self.acno = acno
        self.actype = 'Saving'
        self.bal = 0.00
        print("init by Account class by super")
        super().__init__()
        
    def getAccount(self):
        print("********Account Details**************")
        print("AC Number:", self.acno)
        print("Bank Balance:", self.bal)
        print("Account Type:", self.actype)
        super().getRBI()
'''
    def deposit(self): 
        # amount = int(input("Enter amount to be deposited: ")) 
        # self.bal = self.bal + amount 
        print("\n Amount Deposited:", self.bal) 

    def withdraw(self): 
        amount = int(input("Enter amount to be withdrawn: ")) 
        if self.bal >= amount and amount <= self.max_wdr:
            self.bal -= amount
            print("\n You Withdrew:", amount) 
            print("Availabel Balance:", self.bal)
        else:
            print("Insuficiant Balance!")
'''



class Customer:                                     #<<<<< Customer >>>>>>>
    def __init__(self):
        self.cname = cname
        self.add = add
        self.mob = mob
        self.dob = dob
        super().__init__() # calling Account class constructor..

    def getCustomer(self):
        print("***************Customer Details***************")
        print("Name :", self.cname)
        print("Address :", self.add)
        print("Mobile :", self.mob)
        print("DOB :", self.dob)
        super().getAccount()
                            # Calling 'getAccount' of 'Account' Class 
              

class SBI(Customer, Account, RBI):
    def __init__(self, minbal, minrate, maxwdr):
        self.minbal = minbal
        self.minrate = minrate
        self.maxwdr = maxwdr
        super().__init__()
        super().getCustomer()
    def check(self):
        if self.minbal >= self.min_bal:
            print("Minimum balance is:", self.minbal)
        else:
            print("Minimum balance is lower than RBI Minimum balance", )    
        if self.minrate < self.min_rate:
            print('Minimum rate of Interest is lower than RBI')
        else:
            print('Minimum rate is:', self.minrate)
sbi = SBI()  
sbi.getCustomer()
sbi.check(5000, 5, 2000)


'''
class BOI(RBI, Customer, Account):
    def __init__(self, min_bal, min_rate, max_wdr):
        self.min_bal = 10000
        self.min_rate = 5
        self.max_wdr = 40000


class PNB(RBI, Account):
    def __init__(self, min_bal, min_rate, max_wdr):
        self.min_bal = 10000
        self.min_rate = 5
        self.max_wdr = 40000
'''