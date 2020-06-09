class Student:
    '''initialization of instances  '''
    def setStudent(self, name, pm, cm, mm):         #student details
        self.name = name
        self.pm = pm
        self.cm = cm
        self.mm = mm
    
    def getStudent(self):                           #getting student's details
        print("\nName of Student is", self.name)
        print("Physics marks:", self.pm)
        print("Chemistry marks:", self.cm)
        print("Maths marks:", self.mm)

        def Result(self):                               #Result(percentage calculation)
            total = self.pm + self.cm + self.mm
            percentage = (total*100)/300
            if percentage>50:
                print(self.name, "passed with", round(percentage, 2),"%")
            else:
                print(self.name,"has failed")
        Result(self)
S1 = Student()

snm = input("enter Student's name :")
phy = int(input("Physics marks : "))
chem = int(input("Chemistry marks : "))
maths = int(input("Maths marks marks : "))

S1.setStudent(snm, phy,chem, maths)
S1.getStudent()
# S1.Result()

