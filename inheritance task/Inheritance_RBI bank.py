class Customer:
    def __init__(self):
        pass

    def custdetails(self,  cust_name,  cust_id,  cust_add):
        self.cust_name=cust_name
        self.cust_id=cust_id
        self.cust_add=cust_add
        print(f'Custmer Name: {cust_name} || Customer ID: {cust_id} || Customer Address: {cust_add}')

class Account:
    def __init__(self):
        print("Account")
        super().__init__()

    def getaccount(self, acco_no, bank):
        self.acc_no = acco_no
        if acco_no[-1] == 'S':
            print("Account Type:- Savings account")
        else:
            print("Account Type:- Current Account")
        self.bank = bank
        print(f'Account Number: {self.acc_no} and Bank Name: {self.bank}')

class Rbi:
    def __init__(self, min_bal=1000, min_rate=4, max_with=10000):
        self.min_bal = min_bal
        self.min_rate = min_rate
        self.max_with = max_with
        super().__init__()

    def get(self):
        print(self.min_bal, self.min_rate, self.max_with)

class Sbi(Rbi, Customer, Account):
    def __init__(self):
        print("*************Welcome to SBI*************")
        super().__init__()

    def check(self, rate, bal, limit, cust_name, cust_id, cust_add, acc_no, initial_balance, bank):
        self.rate = rate
        self.bal = bal
        self.limit = limit
        if(self.rate >= self.min_rate and self.bal >= self.min_bal and self.limit <= self.max_with):
            print("Details updated")
        else:
            self.rate = self.min_rate
            self.bal = self.min_bal
            self.limit = self.max_with
            print(self.rate)
            print(self.bal)
            print(self.limit)
        super().custdetails(cust_name, cust_id, cust_add)
        super().getaccount(acc_no, bank)
        if acc_no[-1] == 'S':
            initial_balance = initial_balance + (self.rate/100) * initial_balance
            print("Interest balance:", initial_balance)
        else:
            print("Current balance:", initial_balance)
class Icici(Rbi):
    def details(self):
        self.rate = self.min_rate
        self.bal = self.min_bal
        self.limit = self.max_with
        super().__init__()

    def check(self, rate, bal, limit):
        #print(self.max_with)
     self.rate = rate
     self.bal = bal
     self.limit = limit
     if(self.rate >= self.min_rate and self.bal >= self.min_bal and self.limit <= self.max_with):
         print("Details updated")
     else:
         self.rate = self.min_rate
         self.bal = self.min_bal
         self.limit = self.max_with
         print(self.rate)
         print(self.bal)
         print(self.limit)

class Pnb(Rbi):
    def details(self):
        self.rate = self.min_rate
        self.bal = self.min_bal
        self.limit = self.max_with
        super().__init__()

    def check(self, rate, bal, limit):
     self.rate = rate
     self.bal = bal
     self.limit = limit
     if(self.rate >= self.min_rate and self.bal >= self.min_bal and self.limit <= self.max_with):
         print("Details updated")
     else:
         self.rate = self.min_rate
         self.bal = self.min_bal
         self.limit = self.max_with
         print(self.rate)
         print(self.bal)
         print(self.limit)
        
s= Sbi()
s.check(6, 2000, 10000, "shekhar", "123", "indore", "11225540202", 500, "SBI")

