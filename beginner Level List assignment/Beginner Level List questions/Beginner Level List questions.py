'''
1) print all even and odd number from the given list

my_list=[1,2,3,4,5,6,7,8,9,10]
'''
my_list=[1,2,3,4,5,6,7,8,9,10]
e_list = []
o_list = []
for num in my_list:
    if num % 2 == 0:
        e_list.append(num)
    else:
        o_list.append(num)

print("Even list:", e_list)
print("Odd list:", o_list)
print("=" * 40)

# =======================================================================
'''
2) print all number from the list which is divisible by 7

my_list=[1,2,3,4,5,6,7,8,9,10,13,14,15,16]
'''
my_list=[1,2,3,4,5,6,7,8,9,10,13,14,15,16]
list1 = []

for i in my_list:
    if i % 7 == 0:
        list1.append(i)
print("Numbers divisible by 7 are:" ,list1)
print("=" * 40)

# =======================================================================
'''
3) print only vowel letter from given string 
  str='Hello, i am ajay, how are you?'
'''
str1 = "Hello, i am ajay, how are you?"
vowels = ['a', 'e', 'i', 'o', 'u']
output = ''
for ch in str1:
    if ch in vowels:
        output = output + ch + ' '
print(f"vowels in '{str1}' are:",output)

print("=" * 40)

# =======================================================================
'''
4) print factorial of given number
   input: 4
   output:120
'''
n = 4
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)

print("=" * 40)
# =======================================================================
'''
5) print sum of all even number beween 1 to 20
'''
for i in range(2, 21):
    if i % 2 == 0:
        print(i, end = ", ")