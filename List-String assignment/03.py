'''
3) Print the following output as per given input
INPUT: A3B5C4
OOUTPUT: AAA BBBBB CCCC
<A3 means A should be print 3 times ,B5 B 5 times and so on>
'''
s = "A3B5C4"
alpha = ""
num = ""
length = len(s)
print("length of string is:", length)
for i in s:
    if i.isalpha():
        alpha = alpha + i
    if i.isdigit():
        num = num + i
print("Alphabets are: ", alpha)
print("Numerical values are:", num)

length_alpha = len(alpha)
print("Length of alphabet is :", length_alpha)

length_num=len(num)
print("Length of number is :", length_num)

if length_alpha == length_num:
    for i in range(length_alpha):
        print(alpha[i] * int(num[i]), end=" ")