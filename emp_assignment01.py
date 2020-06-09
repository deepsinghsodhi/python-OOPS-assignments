class Employee:
    # def __init__(self, name, sal, worktime):
    #     self.name = name
    #     self.sal = sal
    #     self.worktime = worktime    

    def getInfo(self, name, sal, worktime):
        self.name = name
        self.sal = sal
        self.worktime = worktime
        print("Name :", self.name)    
        
        if self.sal < 500 and self.worktime > 6:
            a = self.AddWork()
            print(a+10)
        
        elif self.sal < 500:
            a = self.AddSal()
            print('salary is less than 500 so that +10 incentive :', a)

        elif self.worktime > 6:
            a = self.AddWork() 
            print('worktime is more than 6 so that +5 incentive :', a)

        else:
            print("No incentive; due to less working hrs and more salary:", self.sal)

    def AddSal(self):           #if sal<500 then add 10 else as it is
        self.sal = self.sal + 10
        return self.sal                   
    def AddWork(self):          #if worktime>6 then add 5 else as it is
        self.sal = self.sal + 5   
        return self.sal                   

name = input("enter emp name: ")
sal = int(input("enter salary: "))
whrs = int(input("enter working hours: "))
c1 = Employee()
c1.getInfo(name, sal, whrs)

