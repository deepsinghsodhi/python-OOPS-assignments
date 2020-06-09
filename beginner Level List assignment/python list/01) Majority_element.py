'''

Write a program in Python to find the majority element of an List.
A majority element in an ListA of size n is an element that appears more than n/2 times (and hence there is at most 
one such element).
Expected Output : 
The given Listis : 4 8 4 6 7 4 4 8 
There are no Majority Elements in the given array.
----------------------------------------------------------------------
'''

listA = [4,8,4,6,7,4,4,8]
listB = []
n = len(listA)
major = n / 2
# print(major)
# print("Length of list is", n)
for i in listA:
        

    # if i not in listB:
        
        listB.append(i)
# print(listA)
# print(listB)

# for i in listA:
#     c = listA.count(i)
#     print(c)
#     if c > major:
#         print("majori element is ", i)
#         break
#     else:
#         print("There are no Majority Elements in the given array.")
#         break