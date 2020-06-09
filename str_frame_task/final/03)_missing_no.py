'''
3) Write a program to find the missing number from a given list There are no duplicates in list.
Expected Output :
The given list is : 1 3 4 2 5 6 9 8
The missing number is : 7
'''
l=[1,3,4,2,5,6,9,8]
print("The given list is: ", l)
for i in range(1,10):
    if i not in l:
        print("The missing number is: ",i)