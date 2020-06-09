'''
Write a program in Python to find the number occurring odd number of times in an list. 
All numbers occur even number of times except one number which occurs odd number of times.
Expected Output : 
The given Listis : 8 3 8 5 4 3 4 3 5
The element odd number of times is : 3 
'''

listA = [1,1,2,2,2,3,3,4,4]
list1=[]
for i in listA:
    if i not in list1:
        list1.append(i)
print(listA)
print(list1)
for i in list1:
    c = listA.count(i)
    if c % 2 != 0:
        print("the element count which is odd is:",i)
        # -----------------------------------------------