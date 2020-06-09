'''
5)Create three txt file using Python code with name Name1.txt,Name2.txt and Name3.txt and
 write following String (Separate with one white space)

Name1.txt - Amit Ravi rakesh mahesh suresh mohan prasad vivek harshad virat sachin ashwin 
ravindra jitendra mithun hritik aditya kunal salman ajay

Name2.txt - James Alex Amit Ravi rakesh mahesh John Aderson flintoff

Name3.txt - aditya kunal salman ajay James Alex Amit Ravi shyam ganesh vipul hritik 
Rajendra poorwa ankita abhijeet

WAP to read the contents of all three file and print only unique names.
'''

'''
class Names:
    def write_file(self):
        with open("Name1.txt", "w") as wf:
            write_file = wf.write("Amit Ravi rakesh mahesh suresh mohan prasad vivek harshad virat sachin ashwin ravindra jitendra mithun hritik aditya kunal salman ajay")
        with open("Name2.txt", "w") as wf:
            write_file = wf.write("James Alex Amit Ravi rakesh mahesh John Aderson flintoff")
        with open("Name3.txt", "w") as wf:
            write_file = wf.write("aditya kunal salman ajay James Alex Amit Ravi shyam ganesh vipul hritik Rajendra poorwa ankita abhijeet")
name = Names()
name.write_file()
'''
class UniqueNames:
    all_names = []
    unique_names_list = []
    
    def getName1(self):
        n1 = []
        with open("Name1.txt", "r") as rf:
            Name_list1 = (list(rf.read().split(" ")))
            UniqueNames.all_names.extend(Name_list1)
            print("\nName1 list:", Name_list1, "\n")
            self.getName2()
    
    def getName2(self):
        n2 = []
        with open("Name2.txt", "r") as rf:
            Name_list2 = (list(rf.read().split(" ")))
            UniqueNames.all_names.extend(Name_list2)
            print("Name2 list:", Name_list2, "\n")
            self.getName3()

    def getName3(self):
        n3 = []
        with open("Name3.txt", "r") as rf:
            Name_list3 = (list(rf.read().split(" ")))
            UniqueNames.all_names.extend(Name_list3)
            print("Name3 list:", Name_list3, "\n")
            self.Check_Unique_Names()

    def Check_Unique_Names(self):
        for name in UniqueNames.all_names:
            if UniqueNames.all_names.count(name) > 1:
                pass
            else:
                UniqueNames.unique_names_list.append(name)
        print("List of Unique Names is: ", UniqueNames.unique_names_list)
        
un = UniqueNames()
un.getName1()
