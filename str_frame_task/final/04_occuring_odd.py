'''
4)Write a program to find the number occurring odd number of times in an list
All numbers occur even number of times except one number which occurs odd number of times.
Expected Output :
The given list is : 8 3 8 5 4 3 4 3 5
The element odd number of times is : 3
'''

listA = [1,1,2,2,2,3,3,4,4]
print(listA)
list1=[]
for i in listA:
    if i not in list1:
        list1.append(i)
for i in list1:
    c = listA.count(i)
    if c % 2 != 0:
        print("The element odd number of times is:", i)
# ------------------------------------------------------------------
        

