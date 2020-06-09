'''
vWrite a program in Python to find the number of times (frequency) occurs a given number in an List.
Expected Output : 
The given Listis : 2 3 4 4 4 4 5 5 5 6 7 7 
Enter no to check frequency:4
The number of times the number 4 occurs in the given Listis: 4 
'''
l = [2,3,4,4,4,4,5,5,5,6,7,7]
print(l)
num=int(input("enter the number you want to check the frequency: "))
if num in l:
    print("The number", num, "occurs", l.count(num), "times in the given list")
else:
    print("invalid input")