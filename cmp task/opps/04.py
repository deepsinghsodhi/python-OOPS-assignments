'''
4) Create a class named 'Member' having the following members:
Data members
1 - Name
2 - Age
3 - Phone number
4 - Address
5 - Salary
It also has a method named 'printSalary' which prints the salary of the members.
Two classes 'Employee' and 'Manager' inherits the 'Member' class. The 'Employee' and 'Manager' 
classes have data members 'specialization' and 'department' respectively. Now, assign name, age, 
phone number, address and salary to an employee and a manager by making an object of both of these 
classes and print the same.
'''
class Member:
    def __init__(self, name, age, mob, add, sal):
        self.name = name
        self.age = age
        self.mob = mob
        self.add = add
        self.sal = sal
        
        print('Nane:', self.name)
        print('Age:', self.age)
        print('Mob:', self.mob)
        print('Address:', self.add)
    
    def PrintSal(self):
        print('Salary :', self.sal)
    
class Employee(Member):
    def __init__(self, name, age, mob, add, sal, specialization):
        print("----Employee Details----")
        self.specialization = specialization
        self.name = name
        super().__init__(name, age, mob, add, sal)
        print('Specialization:', self.specialization)
        super().PrintSal()

class Manager(Member):
    def __init__(self, name, age, mob, add, sal, department):
        print("----Manager Details----")
        self.department = 'sales'
        self.name = name
        super().__init__(name, age, mob, add, sal)
        print('Department: ', self.department)
        super().PrintSal()

while True:
    print(">>>>>For Employee")
    ename = input("Enter Employee's Name:")
    eage = int(input("Enter Employee's Age:"))
    emob = int(input("Enter Employee's Number:"))
    eadd = input("Enter Employee's Address:")
    esal = int(input("Enter Employee's salery:"))
    spec = input("Enter Employee's Specialization:")


    print('*'*25)

    e1 = Employee(ename, eage, emob, eadd, esal, spec)
    # e2 = Employee(ename, eage, emob, eadd, esal, spec)

    print('*'*25)

    print(">>>>>For Manager")
    mname = input("Enter Manager's Name:")
    mage = int(input("Enter Manager's Age:"))
    mmob = int(input("Enter Manager's Number:"))
    madd = input("Enter Manager's Address:")
    msal = int(input("Enter Manager's salery:"))
    dep = input("Enter Manager's Department:")

    m1 = Manager(mname, msal, mmob, madd, msal, dep)
    # m2 = Manager(mname, msal, mmob, madd, msal, dep)

    print('*'*25)
