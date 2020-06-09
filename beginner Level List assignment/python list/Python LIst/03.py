'''
Write a program in Python to find the missing number from a given list. There are no duplicates in list.
Expected Output : 
The given Listis : 1 3 4 2 5 6 9 8 
The missing number is : 7 
'''
l = [1,3,4,2,5,6,9,8]
print(l)
for i in range(1,10):
    if i not in l:
        print("missing element is:",i, "in list", l )


# num=int(input("enter the number you want: "))
# if num in l:
#     print("The number",num,"occurs",l.count(num),"times in the given list")
# else:
#     print("invalid input")