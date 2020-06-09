'''
2)Write a program which will accept a single pair of strings separated by a comma; 
the program should calculate the sum of ascii values of the characters of each string. 
The program should then subtract the sum of the ascii values of the second string from 
the sum of the ascii values of the first string.

Suppose the following valut is given to the program: 

123ABC,456DEF   

Then the sum of the ascii values of the characters in '123ABC' is 348 and in '456DEF' it is 366. The Difference
 between these numbers is 348 – 366 = -18 
The corresponding output to be printed by the program is: 
-18

HINT: 
myvar = 'A'
print("The ASCII value of '" + myvar + "' is", ord(myvar))#65 '''
# =========================================================================

val = input("Enter two strings with comma separation:")
val_list = val.split(',')    #Spliting the inputs with comma.
s1 = 0 ; s2 = 0
n1 = len(val_list[0])
n2 = len(val_list[1])

for i in range(n1):
    s1 += ord(val_list[0][i])
print(f"ASCII Value of '{val_list[0]}' is: {s1}")
for i in range(n2):
    s2 += ord(val_list[1][i])
print(f"ASCII Value of '{val_list[1]}' is: {s2}")
Difference = s1 - s2
print(f"The Difference of {s1} and {s2} is:", Difference)