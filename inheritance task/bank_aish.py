class Customer:
    def __init__(self):
        print("Constructor customer")


    def custdetails(self, custname, custid, custadd):
        self.custname=custname
        self.custid=custid
        self.custadd=custadd
        print(f'Custname:{custname},custid:{custid},custadd:{custadd}')


class Account:
    def __init__(self):
        print("Account")
        super().__init__()

    def getaccount(self,accono,bank):
        self.accno= accono
        if accono[-1] == 'S':
            print("Savings account")
        else:
            print("Current Account")
        self.bank = bank
        print(f'Accno:{self.accno} and bank: {self.bank}')


class Rbi:
    def __init__(self,minbal=1000,minrate=4,maxwith=10000):
        self.minbal = minbal
        self.minrate= minrate
        self.maxwith=maxwith
        super().__init__()

    def get(self):
        print(self.minbal,self.minrate,self.maxwith)

class Sbi(Rbi,Customer,Account):
    def __init__(self):
        print("SBI")
        super().__init__()


    def check(self,rate,bal,limit,custname,custid,custadd,accno,initial_balance,bank):
        #print(self.maxwith)
     self.rate=rate
     self.bal=bal
     self.limit=limit
     if(self.rate>=self.minrate and self.bal>=self.minbal and self.limit<=self.maxwith):
         print("Details updated")
     else:
         self.rate = self.minrate
         self.bal = self.minbal
         self.limit = self.maxwith
         print(self.rate)
         print(self.bal)
         print(self.limit)
     super().custdetails(custname, custid, custadd)
     super().getaccount(accno, bank)
     if accno[-1] == 'S':
         initial_balance = initial_balance + (self.rate/100)*initial_balance
         print("Interest balance",initial_balance)
     else:
         print("Current balance",initial_balance)
class Icici(Rbi):
    def details(self):
        self.rate= self.minrate
        self.bal=self.minbal
        self.limit=self.maxwith
        super().__init__()

    def check(self,rate,bal,limit):
        #print(self.maxwith)
     self.rate=rate
     self.bal=bal
     self.limit=limit
     if(self.rate>=self.minrate and self.bal>=self.minbal and self.limit<=self.maxwith):
         print("Details updated")
     else:
         self.rate = self.minrate
         self.bal = self.minbal
         self.limit = self.maxwith
         print(self.rate)
         print(self.bal)
         print(self.limit)

class Pnb(Rbi):
    def details(self):
        self.rate= self.minrate
        self.bal=self.minbal
        self.limit=self.maxwith
        super().__init__()

    def check(self,rate,bal,limit):
     self.rate=rate
     self.bal=bal
     self.limit=limit
     if(self.rate>=self.minrate and self.bal>=self.minbal and self.limit<=self.maxwith):
         print("Details updated")
     else:
         self.rate = self.minrate
         self.bal = self.minbal
         self.limit = self.maxwith
         print(self.rate)
         print(self.bal)
         print(self.limit)

s= Sbi()
"""q= Icici()
r= Pnb()
c= Customer()
c.custdetails("dwd","swssS",'dwdbwjd')
a= Account()

s.details()"""
s.check(6,2000,10000,"sdghd","hehue","hwegdye","14252636S",400,"SBI")
"""q.check(4,2200,1000)
r.check(5,4000,10000)"""