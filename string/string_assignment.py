
# 1)Write a python program to reverse a string without using built in methods

A = 'python'
i = len(A) - 1
output = ''
while i >= 0:
    output = output + A[i]
    i = i - 1
print(f"1) Reverse of {A} is:", output)
print("=" * 40)
# ================================================================================

'''2)Write a function that takes an email address as argument, parses it and guesses 
the first and last name from the email address and returns as a tuple. As an example,
 if email address is mukesh.kumar@gmail.com, the function should return (Mukesh, Kumar). 
'''
a = 'mukesh.kumar@gmail.com'
a = a.split('@')
a = str(a[0])
a = a.split('.')
print("2) First Name || Last Name",tuple(a))
print("=" * 40)

# ================================================================================

# 3) Find the first repeated character in a string. For example, if input is "john doe", output would be "o"

a = 'john deo'
b = []

for ch in a:
    if ch not in b:
        b.append(ch)
    else:
        print(f"3) {ch} is repeating in this string")
        break
print('=' * 40)

# ================================================================================

'''
4) Write a program to decrypt a given phrase
  The code in this case is a phrase made from the first letter of each word in the given phrase.
  Input: "his elephant licked lots of wet orange round liquid droplets"
  Output:  helloworld	
  '''

encrypt = "his elephant licked lots of wet orange round liquid droplets"
decrypt = ''
a = encrypt.split(' ')
for ch in a:
    decrypt = decrypt + ch[0]
print(f"4) Decrypted word of '{encrypt}' is:", decrypt)
print("=" * 40)
# ================================================================================
'''
5) take two string from user and check each charactor present in another or not . 
  eg: str1='BLUE' str2='LBUE'   output: matched    
'''
print("5)")
str1 = input("Enter First string: ")
str2 = input("Enter Second string: ")
p = 0
for s in range(len(str1)):
    for s1 in range(len(str2)):
        if(str2[s1] == str1[s]):
            p += 1
            break

if(p == len(str1)):
    print(f"All characters in {str1} are matched with {str2}")
else:
    print("Not matched")
