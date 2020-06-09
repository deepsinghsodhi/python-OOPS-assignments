# arithmetic operator example
'''
a=1
print("before the value of a was :",a)
a=a+1 # addition 
print("after opeartion the value of a is :",a)

a=5
a=a-2 # substraction
print(a)

a=2
a=a*3 # multiplication
print(a)

a=10
a=a/2 # division
print(a)

a=10
a=a%3 # modulus
print(a)

a=10
a=a//2 # floor division
print(a)

a=5
a=a**2 # exponentiation
print(a)
'''

# assignment operator example
'''
a=1
print("value of a is :",a)
a+=2
print("value of a after using assignment operator is :",a)
'''

# logical operators
'''

a=4 # AND 
print(a<10 and a>3) # return true if both the conditions if true

a=2 # OR 
print(a>20 or a<10) # return true if any one condition is true

a=4 # AND 
print(not(a<10 and a>3)) # return true if ans is false and viceversa
'''
# type casting
'''
a=10
print(type(a)) # integer type

a=str(a) # type casting

print(type(a)) # string type
'''
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.
'''
for i in range(1500,2700):
    if i%5==0 and i%7==0:
        print("number is :",i)
'''
# Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
s=(1,2,3,4,5,6,7,8,9)
even_count=0
odd_count=0
for i in s:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("total odd numbers in series is:",odd_count)
print("total even numbers in series is :",even_count)
'''
# Write a Python program that accepts a word from the user and reverse it.
'''
name=input("enter any string")
print("reverse of string is:",name[::-1])
'''
# Write a Python program to count the number of even and odd numbers from a series of numbers. 
'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0
for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("total even is:",even)
print("total odd is:",odd)
'''
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
for i in range(7):

    if i==3 or i==6:
        print("pass",end="")
        continue
    print(i,end="")
'''
# fibonacci series
'''
num1=0
num2=1
print(num1,end=" ")
print(num2,end=" ")
for i in range(2,51):
    num3=num1+num2
    print(num3,end=" ")
    num1=num2
    num2=num3
'''
# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and
#for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
'''
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        continue
    elif i%3==0:
        print("fizz")
        continue
    elif i%5==0:
        print("buzz")
        continue
    print(i)
    
'''
# 14. Write a Python program that accepts a string and calculate the number of digits and letters.
'''
data=input("enter any string")
dig_count=0
letr_count=0
for i in data:
    if i.isdigit():
        dig_count+=1
    elif i.isalpha():
        letr_count+=1
    else:
        pass
print("total digit in the string is:",dig_count)
print("total letters in the string is:",letr_count)
'''
'''
l=[]
for i in range(100,401):
    s=str(i)
    if (int(s[0]%2==0)) and (int(s[1]%2==0)) and (int(s[2]%2==0)):
        print(l.append(s))

'''
#
'''
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
#print(items)
print( ",".join(items)) # join method converts list into string format
'''
#  32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
'''
s=input("enter any single character: ")
if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
    print(s,": is a vowel")
else:
    print(s,": is an consonent")
'''
# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''
num1=int(input("enter number 1 : "))
num2=int(input("enter second number: "))
sum=num1+num2
if sum in range(15,21):
    print(20)
else:
    print(sum)
'''
#OR
'''
def show(x,y):
    sum=x+y
    if sum in range(15,21):
        return 20
    else:
        return sum

num1=int(input("enter number 1 : "))
num2=int(input("enter second number: "))
print(show(num1,num2))
'''
# multipliaction table
'''
num=int(input("enter any number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
'''
# pattern
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,end="")
    print()
        
'''
# reverse of collection
'''
a="systango" # string allows slicing
print(a[::-1])

l=[10,20,30] # list allows slicing
print(l[::-1])

s=(10,20,30,40) # tuple allows slicing
print(s[::-1])

t={10,20,30,40,50} # set dont allows slicing 
print(t[::-1]) 
'''

'''
l=[10,20,30,40,50,60]
#print(l[3])
#print(l[:3]) # 10,20,30

#print(l[3:]) # 40,50,60

#print(l[-2]) # 50

#print(l[::-2]) # 60 40 20
'''
#====================================
#====================================
#====================================
'''
a={'one':'two'}
b=a
b['two']='test'
b['one']='zero'
print(a)
print(b)
'''

'''
a=10
b=a
b=20
print(a)
'''

# square root of any number
'''
from math import *
num=int(input("enter number to find it's square root: "))
root=sqrt(num)
print("square root of",num,"is:",root)


num=int(input("enter number to find it's square root: "))
root=num**(1/2)
print("square root of",num,"is:",root)
'''

# pattern
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()


k=1
for i in range(1,4):
    for j in range(1,k+1):
        print("@",end=" ")
    k=k+2
    print()
    

k=2
for i in range(1,4):
    for j in range(1,k+1):
        print("@",end=" ")
    k=k+2
    print()
    

for i in range(65,70):
    for j in range(1,6):
        print(chr(i),end=" ")
    print()
    

for i in range(1,6):
    for j in range(65,70):
        print(chr(j),end=" ")
    print()


for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
    

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()


k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


for i in range(5,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
    

num=int(input("enter number of rows you want"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()


num=int(input("enter numbre of rows for pyramid"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()


num=int(input("enter number of rows for pyramid"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print()


num=int(input("enter number of rows for pyramid"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()


for i in range(5,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
    

num=int(input("enter the numver of rows you want in yiur diamond"))
for i in range(0,num):
    print(" "*(num-i-1)+"* "*(i+1))
for j in range(num-1,0,-1):
    print(" "*(num-j)+"* "*(j))
'''
#==========================================
'''
s="jjojhn doe"
print("original string is:",s)
for i in s:
    if s.count(i)>1:
        print("repeated char is:",i)
        break
''' 
#==========================================
'''
s="ram narayan"
s1=s.capitalize()
print(s1)

s="KANAK DAUR"
s1=s.casefold()
print(s1)

s="hello world"
s1=s.center(50)
print(s1)

s="kanak is kanak but she is not kanak"
s1=s.count("she")
print(s1)

s="kanak is kanak but she is not kanak"
s=s.endswith("not")
print(s)

s="mere angne main tumhara kya kaam h"
s=s.startswith("kya")
print(s)

s="k\ta\tn\ta\tk"
s=s.expandtabs(5)
print(s)

s="kanak is kanak but she is not kanak"
s=s.find("n")
print(s)

txt = "For only {price} dollars!"
print(txt.format(price = 49))

s="my name is {name}...hello everyone"
inp=input("enter name: ")
s=s.format(name=inp)
print(s)

s="rohan"
s=s.index("o")
print(s)

s="   "
s=s.isspace()
print(s)

s="Kanak Daur"
s=s.istitle()
print(s)

l=["kanak","daur"]
print(l)
l1=" ".join(l)
print(l1)


s="    kanak"
print(s)
s=s.lstrip()
print(s)

s="kanak         "
print(s)
s=s.rstrip()
print(s)

s="  kanak   "
print(s)
s=s.strip()
print(s)

s="my name is kanak daur"
s=s.rpartition("my")
print(s)

s="kanak"
s=s.replace("k","s")
print(s)

s="home.java"
print(s)
s=s.split(".")
l=len(s)
print("extension of file is :",s[l-1])

s="hello moto\nsamsung is best"
s=s.splitlines()
print(s)

'''
#======================================= blue = lueb==========
'''
str1=input("enter first string: ")
str2=input("enter second string: ")
print("first string is:",str1)
print("second string is:",str2)
len1=len(str1)
print("length of first string is:",len1)
len2=len(str2)
print("length of second string is:",len2)
if len1==len2:
    for i in range(len1):
        if str1[i] in str2:
            print("matched")
            break
'''
#====================================== character frequency=============
'''
s="google"
length=len(s)
list1=[]
list2=[]
for i in range(length):
    if s[i] not in list1:
        list1.append(s[i])
    list2.append(s[i])
print("list 1 is:",list1)
print("list2 is:",list2)
for i in list1:
    c=list2.count(i)
    print(i,":",c)
'''
# character frequency ==================================================
'''
a="google.com"
print("original string is:",a)
s=""
for i in a:
    if i not in s:
        s=s+i
print("the unique elemets of string are: ",s)
for i in s:
    c=a.count(i)
    print(i,":",c)
'''
# swap the cases of the string =========================================

#s="kAnAk"
'''
s1=""
s=s.swapcase()
print(s)
'''
#=== OR ======
'''
for i in s:
    if i.isupper():
        s1=s1+i.lower()
    elif i.islower():
        s1=s1+i.upper()
print(s1)
'''
#======================================================================= DOUBT===
'''
s="restart"
char=s[0]
s=s.replace(char,"@")
s=char+s[1:]
print(s)
'''
# reverse of words present in a string 
'''
s="one two three"
print(s)
s=s.split()
s=s[::-1]
s1=" ".join(s)
print(s1)
'''
# revesre of string using slicing operator
'''
s="rajat"
s=s[::-1]
print(s)
'''
# reverse of string using reversed method
'''
s="shekhar"
s1=reversed(s)
for i in s1:
    print(i,end="")
'''
# reverse of string using loop
'''
s="poonam"
output=""
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)

# list
l=[10,50,70,30,10]
l.sort(reverse=True)
print(l)
'''
# sum of all elemnts present in a list
'''
l1=[]
num=int(input("enter how many elemnts you want in your list"))
for i in range(num):
    ele=int(input("enter elemnt"))
    l1.append(ele)
print(l1)
sum=0
for i in l1:
    sum=sum+i
print("sum is:",sum)
'''
# multipliaction of all elemnts present in a list
'''
l=[2,3,5]
mul=1
for i in l:
    mul=mul*i
print("multiplication of all is:",mul)
'''
# print the greatest number from a list
'''
l=[2,8,4,9,15,78,3,1]
l.sort()
print(l)
leng=len(l)
print("greatest number is list is:",l[leng-1])
'''
# # print the smallest number from a list
'''
l=[2,8,4,9,15,78,3,1]
l.sort()
print(l)
print("smallest number in list is:",l[0])
'''
#  Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
'''
l=['abc', 'xyz', 'aba', '1221']
count=0
for i in l:
    if len(i)>2 and i[0]==i[-1]:
        count=count+1
        print("valid elemnt",i)
    else:
        print("invalid list elemnts",i)
'''
#=======================
'''
l=[8,3,8,5,4,3,4,3,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l)
print(l1)
for i in l1:
    c=l.count(i)
    if c%2!=0:
        print("the element count which is odd is:",i)
'''
#====================================================
'''
l=[1,3,4,7,5,6,9,8]
for i in range(1,10):
    if i not in l:
        print("missing element is:",i)
'''
#=====================================================
'''
l=[2,3,4,4,4,4,5,5,5,6,7,7]
print(l)
num=int(input("enter the number you want: "))
if num in l:
    print("The number",num,"occurs",l.count(num),"times in the given list")
else:
    print("invalid input")
'''
#======================================================
'''
l=[1,3,4,7,5,6,9,8]
length=len(l)
i=0
for x in l:
    print("positive index: ",i,"and neagtive index is: ",i-length,"of number: ",x)
    i+=1
'''    
#=====================================================
'''
l=[1,3,4,7,5,6,9,8]
print(l)
length=len(l)
num=int(input("enter any number from the list"))
if num in l:
    print("positive index is:",l.index(num))
    print("neagtive index is:",(l.index(num))-length)
'''
#=====================================================
'''
l=[]
num=int(input("enter how many numbers you want in your list "))
for i in range(1,num+1):
    print("enter",i,"element")
    ele=int(input())
    l.append(ele)
print(l)
'''
#=======================================================
'''
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in i:
        print(j,end="")
    print()
'''
#========================================================= list comprehension 
'''
l=[ x for x in range(1,50) if x%2==0]
print(l)
'''
# list comprehension =====================================
'''
l=[1000,5000,3000,8000,4000]
l1=[i+500 for i in l if i<5000]
print(l1)
'''
#===========================================================
'''
l=[]
if len(l)==0:
    print("list is empty")
'''
#===========================================================
'''
x=("apple","banana","cherry")
#print(type(x))
print("given tuple is:",x)
y=list(x)
#print(type(y))
#print("converted list is:",y)
y[0]="zero"
#print(y)
x=tuple(y)
print("updated tuple is:",x)
'''
#===========
'''
l=[10]
print(type(l))
t=(50,)
print(type(t))
'''
#=================
'''
t=(10,20,80,70,60)
t1=sorted(t)
t2=tuple(t1)
print(t2)
print(type(t2))

l=[50,70,20,90,40,30,10,60]
l.sort(reverse=True)
print(l)

s="rajat"
s=reversed(s)
for i in s:
    print(i,end="")

l=["kanak","daur"]
l.reverse()
print(l)
'''
#==== packing =========
'''
a=10
b=20
c=30
pack=a,b,c
print(pack)
print(type(pack))
'''
#===== unpacking =======
'''
x,y,z=100,120,150
xyz=x,y,z
print(x)
print(z)
'''
#======================== tuple comprehension =======
'''
t=( x for x in range(1,21) if x%2==0)
print(t)
'''
#======================= set
'''
s={"one","two","three","four","five"}
print(s)
'''
#=======================
'''
s={"one","two","three","four","five"}
for i in s:
    print(i)
'''
#======================
'''
s={"one","two","three","four","five"}
print("two" in s)
'''
#=======================
'''
s={"one","two","three","four","five"}
s.add("mango")
print(s)
'''
#=======================
'''
s={"one","two","three"}
s1={"apple","mango"}
s.update(s1)
print(s)
'''
#=======================
'''
s={"one","two","three","four","five"}
print("length of set is:",len(s))
'''
#=======================
'''
s={"one","two","three","four","five"}
s.remove()
print(s)
'''
#=====================
'''
s={"one","two","three","four","five"}
s.discard("kanak")
print(s)
'''
#=====================
'''
s={"one","two","three","four","five"}
s1=s.pop()
print(s1)
print(s)
'''
#======================
'''
s={"one","two","three","four","five"}
s.clear()
print(s)
'''
#======================
'''
s={"one","two","three","four","five"}
del s
print(s)
'''
#=====================
'''
s={1,2,3}
s1={4,5,6}
s=s.union(s1)
print(s)
'''
#====================
'''
s={"one","two","three","four","five"}
s1=s.copy()
print(s1)
'''
#====================
'''
s={10,20,30}
s1={30,40,50}
s=s.intersection(s1)
print(s)
'''
#===================== sub set 
'''
s={10,20,30}
s1={50,10,80,20,90,30,40}
s=s.issubset(s1)
print("matched")
'''
#==================== super set
'''
s={10,50,80,60,30,70}
print(s)
s1={10,20,30,70}
print(s1)
s=s.difference(s1)
print(s)
'''
#=============================
'''
s={"one","two","three"}
s1={"four","five","three"}
s=s.symmetric_difference(s1)
print(s)
'''
#======================
'''
s={5,8,2,6,7}
print("given set is:",s)

print("maximun value in set is:",max(s))
print("minimum value in set is:",min(s))

max=0
min=9
for i in s:
    if i>max:
        max=i
for i in s:
    if i<min:
        min=i
print("maximum value of set is:",max)
print("minimum value of set is:",min)
'''
#==================== user input of set ====
'''
s=[]
num=int(input("enter the number of elemnts you want in your set"))
for i in range(num):
    ele=eval(input("enter elemnts")) 
    s.append(ele)
s1=set(s)
print(type(s1))
print(s1)
'''
#===============================

'''
print(d["city"])
d["city"]="ratlam"
print(d)
d["subject"]="python"
print(d)
for i in d.values():
    print(i)
   
for i,j in d.items():
    print(i,":",j)

if "age" in d:
    print("yes..its is present in the dictionary")

length=len(d)
print("length of the dictionary is:",length)

d.clear()
print(d)
print(type(d))

d1=d.copy()
print(d1)

one={"name","age","city"}
two="kanak"
thisdict=dict.fromkeys(one,two)
print(thisdict)

d1=d.items()
print(d1)

d2=d.keys()
print(d2)

print(d)
d1=d.pop("city")
print(d1)
print(d)

d.popitem()
print(d)

d={"name":"kanak",
   "age":"20",
   "city":"indore",
   "subject":"python"}
d.update({"one":101,"two":102})
print(d)
d1=d.values()
print(d1)

nestdic={
    "child1":{
        "name":"kanak",
        "age":20
        },
    "child2":{
        "name":"shekhar",
        "age":24
        },
    "child3":{
        "name":"rajat",
        "age":14
        },
    }
for i,j in nestdic.items():
    print(i,j)


dict1=dict(id1=101,name="kanak")
print(dict1)
'''
# Write a Python script to concatenate following dictionaries to create a new one. 
'''
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
for i,j in dic4.items():
    print(i,":",j)

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d1.update(d2)
print(d1)


d1 = {'a': 100, 'b': 200,'c': 300}
sum=0
for i in d1.values():
    sum=sum+i
print("sum of all values is:",sum)

dict1={2:"two",6:"six",9:"nine",3:"three"}
for i in sorted(dict1):
    print(i,":",dict1[i])

dict1={"two":2,"six":6,"nine":9,"three":3}
l=[]
for i in dict1.values():
   l.append(i)
print(l)

print("maximun value:",max(l))
print("minimum value :",min(l))
'''
#=========== function =====================
'''
def show(name):
    print(name,"show is running")
show("hello")
'''
#===== positional argument in function of python =============
'''
def add(a,b):
    print("the value of a is:",a)
    print("the value of b is:",b)
    c=a+b
    print("sum of both values is:",c)
add(5,4)
'''
#====== keyword argument in functions of python =============
'''
def display(name,age):
    print("my name is:",name)
    print("my age is:",age)
display(age=20,name="kanak")
'''
#====== default argument in function of python ============
'''
def default(city="indore"):
    print("city name is:",city)
default("ratlam")
'''
#====== variable length argument in function of python ========
'''
def varlen(*k):
    for i in k:
        print(i)
varlen(10,20,30)
'''
# === keyword variable length argument in python functions ==============
'''
def disp(**kwargs):
    print("information details")
    for i,j in kwargs.items():
        print(i,":",j)
disp(name="kanak",sal=50000,eid=101)
'''
#== factorail program using function ===================================
'''
def fact(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    print("factorail value of",num,"is",fact)
num=int(input("enter number to find its factorial"))
fact(num)
'''
#============ majority element =============
'''
l=[2,8,2,6,7,2,2,8]
lnew=[]
n=len(l)
major=n//2
print("majority value is:",major)
print("length of the list is: ",n)
for i in l:
    if i not in lnew:

        lnew.append(i)
print(l)
print(lnew)
for i in lnew:
    c=l.count(i)
    if c>=major:
        print("majority element is:",i) # 2 is the answer
        '''
#======= recursion : factorial program ====================
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result=fact(5)
print("factorail value is:",result)
'''
# ==========================================================
'''
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

num=int(input("enter number: "))
print(fact(num))
'''
#=========================================================
'''
def table(num):
    def multiple(mul):
        if mul==11:
            pass
        else:
            return num*multiple(mul+1)

    multiple(1)
num=int(input("enter number to print the multipliaction table: "))
print(table(num))
'''
#===== sum of all numbers ==============================
'''
def countall(num):
    if num<=0:
        return num
    else:
        return num+countall(num-1)
num=int(input("enter number"))
print(countall(num))
'''
#======== multipliaction table using recursion =========
'''
def table(num,i):
    if i>10:
        return 1
    else:
        print(num*i)
        table(num,i+1)
num=int(input("enter number to print its table :"))
table(num,1)
'''
'''
def table(num,i):
    if i>10:
        return 1
    else:
        print(num*i)
        table(num,i+1)
num=int(input("enter number: "))
table(num,1)
'''
#===========
'''
def show(num):
    if num>10:
        return 1
    else:
        print("kanak",num)
        show(num+1)
show(5)
'''
#============= reverse of numbers using recursion ===========
'''
def reverse(num):
    if num<1:
        return 1
    else:
        print(num)
        reverse(num-1)
num=int(input("enter number"))
reverse(num)
'''
#=========== table till input number =======================
'''
l=[]
num=int(input("enter number to end"))
for i in range(1,num+1):
    l.append(i)
for i in l:
        m=1
        while m<=10:
            print(i*m,end=" ")
            m=m+1
        print()
        
'''
#============ factorial using recursion ===================
'''
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter number"))
print(fact(num))
'''
#=========== sum of all numbers using recursion ===========
'''
def addall(num):
    if num<=0:
        return num
    else:
        return num+addall(num-1)
num=int(input("enter number"))
print(addall(num))
'''
#=========== multipliaction table using recursion ==========
'''
def table(num,i):
    if i>10:
        return 1
    else:
        print(num*i)
        table(num,i+1)
num=int(input("enter number to print it's table: "))
table(num,1)
'''
#========== reverse of numbers using recursion =============
'''
def reverse(num):
    if num<1:
        return 1
    else:
        print(num)
        reverse(num-1)
num=int(input("enter number "))
reverse(num)
'''
#========== fibonacci series using recursion ===============
'''
def fib(num1,num2,n):
    if n==0:
        return 1
    else:
        num3=num1+num2
        print(num3,end=" ")
        fib(num2,num3,n-1)
a=0
b=1
n=int(input("enter number"))
print(a,end=" ")
print(b,end=" ")
fib(a,b,n-2)
'''
#========== anonymous function ================================
'''
x=lambda a:a+10
print(x(5))

y=lambda x,y:x*y
print(y(4,5))

z=lambda a,b,c:a+b+c
print(z(1,2,3))

def myfun(num):
    return lambda a:a*num
mydoubler=myfun(5)
print(mydoubler(4))

f=lambda x:x*x*x
num=int(input("enter number: "))
result=f(num)
print(result)
'''
#=========== lambda function ===================================
'''
f=lambda a:a+15
num=int(input("enter number: "))
print(f(num))
'''
# filter map and reduce =====================
'''
l=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,l))
print(even)

double=list(map(lambda x:x*2,even))
print(double)

from functools import reduce
addall=reduce(lambda x,y:x+y,even)
print(addall)
'''
#======== map function=============
'''
one=[1,2,3,4,5]
print(one)
two=[1,1,1,1,1]
print(two)
addall=list(map(lambda x,y:x+y,one,two))
print("sum of both list is: ",addall)
'''
#==========3) Print the following output as per given input
'''
INPUT: A3B5C4
OOUTPUT: AAA BBBBB CCCC
<A3 means A should be print 3 times ,B5 B 5 times and so on>
'''
#======== shekhar task ================================
'''

s="A3B5C4D7"
alpha=""
num=""
length=len(s)
print("length of string is:",length)
for i in s:
    if i.isalpha():
        alpha=alpha+i
    if i.isdigit():
        num=num+i
print(alpha)
print(num)

length_alpha=len(alpha)
print("length of alpha :",length_alpha)

length_num=len(num)
print("length of number :",length_num)

if length_alpha==length_num:
    for i in range(length_alpha):
        print(alpha[i]*int(num[i]),end=" ")

'''
#============ lambda practice =============================
# Write a Python program to sort a list of tuples using Lambda.
'''

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)
'''
# Write a Python program to sort a list of dictionaries using Lambda.
'''
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)
'''
# Write a Python program to filter a list of integers using Lambda.
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list ")
print(nums)

even_nums=list(filter(lambda x:x%2==0,nums))
print("\n list of even numbers ")
print(even_nums)

odd_nums=list(filter(lambda x:x%2!=0,nums))
print("\n list of odd numbers ")
print(odd_nums)
'''
#  Write a Python program to square and cube every number in a given list of integers using Lambda
'''
l=[1,2,3,4,5]
print("original list ")
print(l)

square=list(map(lambda x:x*x,l))
print("\n square of all elemnts of list ")
print(square)

cube=list(map(lambda x:x*x*x,l))
print("\n cube of all elemnts of list ")
print(cube)
'''
# Write a Python program to find whether a given string starts with a given character using Lambda.
'''
name=lambda x:"name is:"+x if x.startswith("p") or x.startswith("k") else "invalid name"
n=input("enter any string: ")
print(name(n))
'''
# Write a Python program to extract year, month, date and time using Lambda.
'''
import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time()
print("year is:",year(now))
print("month is:",month(now))
print("day is:",day(now))
print("time is:",time(now))
'''
# Write a Python program to check whether a given string is number or not, using Lambda.
'''
name=lambda x:"string is a digit" if x.isdigit() or x.isalnum() else "string is alpha"
n=input("enter any string: ")
print(name(n))
'''
#4) Write a  code to find the distance from Mumbai to major cities of India.
'''
city=["indore","mumbai","pune"]
print(city)

dist=[1200,3500,7888]
print(dist)

newlist=dict(zip(city,dist)) # zip will merge all the data of list(city & dict)together according to their position and than convert them into a dictionary

for i,j in newlist.items():
    print(i,":",j)
    
print("enter the city name: ")
c=input()

if c in newlist:
    print(newlist.get(c))
else:
    print("invalid city name")
'''
#======= shekhar's assignment =====================

'''
event_one={1001,1002,1003,1004,1005}
print("id of employees of event 1:")
print(event_one)
event_two={1106,1008,1005,1003,1016,1017,1112}
print("\nid of employees of event 2:")
print(event_two)
print("\ncommon employees ID: ",event_one.intersection(event_two))
'''
# ========= variables of functional programmming ========================
'''
a=10 # global variables
b=20 # global variables
def first():
    c=a+b
    print("sum of a and b is: ",c) 
first()
def second():
    c=a*b
    print("multiplication of a & b is: ",c)
second()

def third():
    global x
    x=50
    global y
    y=40
    z=x+y
    print("sum of x and y is: ",z)
third()

def fourth():
    z=x*y
    print("product of x and y is: ",z)
fourth()

def fifth():
    k=500
    print(k)
fifth()

def sixth():
    k=400
    print(k)
sixth()
'''
list1=[1,2,3,4,5]
# shallow copy using build in functions 
'''
print(list1)
print(type(list1))
list2=set(list1)
print(list2)
print(type(list2))
list2.add(10)
print(list2)
print(list1)
'''
# shallow copy using slicing operator
'''
print(list1)
list2=list(list1[:])
print(list2)
list2.insert(3,30)
print(list2)
print(list1)
'''
# shallow copy using list comprehension
'''
list2=[x for x in list1]
print(list2)
print(list1)
'''
# shallow copy using copy method of python
'''
list2=list1.copy()
print("list1 is:",list1)
print("list2 is:",list2)
list2=set(list2)
print(list2)
print(type(list2))
list2.add(60)
print(list2)
print(list1)
'''
# to avoid such type of prblm we will use deep copy to copy compound objects or nested sequence
'''

list2=[[1,2,3],[4,5,6]]
print(list2)
list_new=list2.copy()
print(list_new)
list_new[0][0]="kanak"
print(list_new)
print(list2)
'''
# deep copy method
# to use deepcopy first we will have to import the copy module 
'''
from copy import deepcopy
list2=[[1,2,3],[4,5,6]]
list_new=deepcopy(list2)
print(list2)
print(list_new)
list_new[0][0]="changed"
print(list_new)
print(list2)
'''
# ====== python basic practice questions ====================
'''
start=int(input("enter starting range: "))
end=int(input("enter ending range: "))
for i in range(start,end+1):
    if i%2==0:
        print("\neven number:",i,end=" ")
    else:
        print("\nodd numbers :",i,end=" ")

'''
#
'''
start=int(input("enter the starting range"))
end=int(input("enter the ending range"))
even=0
odd=0
for i in range(start,end+1):
    if i%2==0:
        print(i,end=" ")
        even=even+1
    else:
        print(i,end=" ")
        odd=odd+1
print("\ntotal even is: ",even)
print("\ntotal odd is: ",odd)
'''
#
'''
num=int(input("enter number to find its factorial: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial value is: ",fact)
'''
#
'''
num=int(input("enter number to find fibonacci series till that number: "))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(2,num):
    num3=num1+num2
    print(num3,end=" ")
    num1=num2
    num2=num3
'''
#
'''
i=1
while i<11:
    print(i,end=" ")
    i=i+1
i=10

print()

while i>=1:
    print(i,end=" ")
    i=i-1
'''
#
'''
sum=0
for i in range(1,6):
    sum=sum+i
print("sum of all numbers in a given range is: ",sum)
'''
#
'''
num=int(input("enter any number: "))
sum=0
while num>0:
    dig=num%10
    sum=sum+dig
    num=num//10
print("sum of all numbers is: ",sum)
'''
#
'''
num=123456
num=str(num)
num=num[::-1]
num=int(num)
print(type(num))
print(num)
'''
#
'''
num=int(input("enter any number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("reverse of number is: ",rev)
if temp==rev:
    print("number is pallindrome")
else:
    print("not a pallindrome")
'''
#
'''
num=int(input("enter number: "))
temp=num
sum=0
while num>0:
    dig=num%10
    sum=sum+dig
    num=num//10
print("sum of each digit of number",temp,"is",sum)
'''
#
'''
num=int(input("enter number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("reverse of the number ",temp,"is: ",rev)
'''
#
'''
num=int(input("enter any number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev==temp:
    print(temp,"is a pallindrome")
else:
    print("Number is not a pallindrome")
'''
#
'''
name=input("enter any string: ")
name=name[::-1]
print(name)
'''
#
'''
num=int(input("enter any number: "))
max=0
min=9
while num>0:
    dig=num%10
    if dig>max:
        max=dig
    if dig<min:
        min=dig
    num=num//10
print("maximum value is: ",max)
print("minimum value is :",min)
'''
#
'''
l=[1,2,3,4,5]
print("given list is: ",l)
length=len(l)
i=0
for k in l:
    print("positive index is: ",i,"and negaive index is: ",i-length,"of number : ",k)
    i=i+1
'''
#
'''
num=int(input("enter any number to check it is angstromg or not: "))
temp=num
ang=0
while num>0:
    dig=num%10
    ang=ang+dig*dig*dig
    num=num//10
if temp==ang:
    print(temp,"is a angstrong")
else:
    print(temp,"is not a angstrong")
 ''' 
#
'''
num=int(input("enter number to check it is prime or not: "))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("prime number")
'''
#
'''
for i in range(1,11):
    if i%2==0:
        print("even")
        continue
    print(i)
            
'''
#
'''
for i in range(1,11):
    if i%2!=0:
        print("*",end=" ")
    else:
        print(i,end=" ")
'''
#
'''
for i in range(1,11):
    if i%2!=0:
        print("*",end=" ")
        continue
    print(i,end=" ")
'''
#
'''
s=input("enter any string: ")
s_new=""
for i in s:
    if i not in s_new:
        s_new=s_new+i
print(s)
print(s_new)
for i in s_new:
    c=s.count(i)
    print("count of ",i, "in the given string is:",c)
'''
#
'''
val1=input("Enter Any Number:")
val2=list(val1)
val3=val2[0]
val2[0]=val2[len(val2)-1]
val2[len(val2)-1]=val3
val4="".join(val2)
print("after canges new string: ",val4)
print(type(val4))
'''
#
'''
l=[100,200,300,450,700]
for i in l:
    if i>1000:
        break
else:
    print("all items processed successfully")
'''
#
'''
l=[100,200,300,450,700]
for i in l:
    if i>=500:
        break
    print(i)
else:
    print("all the item processed successfully")
'''
#
'''
name=input("enter any string: ")
name_new=""
for i in name:
    if i not in name_new:
        name_new=name_new+i
print("original string:",name)
print("unique elements of string is:",name_new)
'''
#
'''
s="one two three four"
print(s)
s1=s.split()
#print(s1)
s1=s1[::-1]
#print(s1)
s2=" ".join(s1)
print(s2)
'''
#
'''
import sys
print("current python version is:",sys.version)
print("\ncurrent python version info is: ",sys.version_info)
'''
#
'''
colorlst = ["Red","Green","White" ,"Black"]
l=len(colorlst)
print("length of the list is:",l)
last=l-1
print("first color is:",colorlst[0])
print("last color is:",colorlst[last])
'''
#
'''
file=input("enter any file name: ")
file=file.split(".")
print(file)
length=len(file)
print("extension of file is: ",file[length-1])
'''
#
'''
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1>num2 and num1>num3:
    print("greatest is num1")
elif num2>num3:
    print("greastest is num2")
else:
    print("graetest is num3")
'''
#
'''
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
greatest=max(num1,num2,num3)
smallest=min(num1,num2,num3)
print("greatest is:",greatest)
print("smallest is:",smallest)
'''
#
'''
l=[1,0,1,0,1]
l_new=[]
for i in l:
    l_new.append(int(not(i)))
print(l_new)
'''
#
'''
s="systango pvt ltd"
print(s)
s=s.split()
#print(s)
temp=s[0]
s[0]=s[len(s)-1]
s[len(s)-1]=temp
#print(s)
s=" ".join(s)
print(s)
'''
#
'''
class myclass: # defining class
    name="kanak" # data members (attributes)
    age=20

obj=myclass() # class object
print("Name is : ",obj.name) # accessing data members of class using object 
print("Age is : ",obj.age)
'''
#
'''
class myclass:
    def __init__(self):
        self.name="kanak"
        self.age=20
obj=myclass()
print(obj.name)
print(obj.age)
'''
#
'''
class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
name=input("enter name : ")
age=input("enter age : ")
obj=myclass(name,age)
print("name is : ",name)
print("age is : ",age)
'''
# updating object value
'''
class myclass:
    def __init__(self):
        self.city="indore"
    def myfun(self):
        print("this is member method : ",self.city)
obj=myclass()
obj.city="ratlam"
obj.myfun()
'''
#
'''
class myclass:
    def __init__(self,age):
        self.name="kanak"
        self.age=age
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
age=int(input("enter age : "))
obj=myclass(age)
obj.age=20
obj.show()
'''
# delete attributes from class using objects of that class
'''
class myclass:
    def __init__(self,age):
        self.name="kanak"
        self.age=age
    def show(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
age=int(input("enter age : "))
obj=myclass(age)
del obj.name
obj.show()
'''
# delete object
'''
class myclass:
    name="kanak"
obj=myclass()
obj1=myclass()
del obj
print("object 2",obj1.name)

print("object 1",obj.name)
'''
#============================================================================================================================================================
'''
def show(x,y): # function defination
    """This function to add two numbers """ # docstring
    return x+y # function return type
print(show(5,4)) # function calling
print(show.__doc__) # print the docstring

print(max.__doc__) # we can also the docstring of in bulid functions in this way 
'''
'''
l=[1,0,1,0,1]
m=[]
for i in l:
    m.append(int(not i))
print(m)
'''
#
'''
print("<------- Rock paper & Scissors game -------->")

print(" \nOptions available for the user to choose from \n\n 1 -> Rock\n 2 -> Paper\n 3 -> Scissor")

print("\n Winning combinations are follows :")

print("\n Rock Vs Rock = Tie")
print(" Rock Vs Paper = paper won")
print(" Rock Vs Scissors = Rock won")

print("\n Paper Vs Rock = paper won")
print(" Paper Vs Paper = Tie")
print(" Paper Vs Scissors = scissor won")

print("\n Scissors Vs Rock = Rock won")
print(" Scissors Vs Paper = Scissor won")
print(" Scissors Vs Scissors = Tie")

print("\n===============================================")

comp_wins=0
player_wins=0

def player_option():
    user_choice=int(input("\nEnter your choice (In nummber) : "))
    print()
    if user_choice == 1:
        user_choice = "rock"
    elif user_choice == 2:
        user_choice = "paper"
    elif user_choice == 3:
        user_choice = "scissor"
    else:
        print("invalid input")
        player_option()
    return user_choice


def computer_option():
    import random
    comp_choice=random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "rock"
    elif comp_choice == 2:
        comp_choice = "paper"
    elif comp_choice == 3:
        comp_choice = "scissor"
    return comp_choice


while True:
    user_choice = player_option()
    comp_choice = computer_option()

    if user_choice == "rock":
        if comp_choice == "rock":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("It's a TIE")
        elif comp_choice == "paper":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("computer won")
            comp_wins+=1
        elif comp_choice == "scissor":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("You won")
            player_wins+=1

    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("You won")
            player_wins+=1
        elif comp_choice == "paper":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("It's a TIE")
        elif comp_choice == "scissor":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("Computer won")
            comp_wins+=1

    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("Computer won")
            comp_wins+=1
        elif comp_choice == "paper":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("You won")
            player_wins+=1
        elif comp_choice == "scissor":
            print("You selected : ",user_choice)
            print("computer selected : ",comp_choice)
            print()
            print("<-------",user_choice,"Vs",comp_choice,"-------->")
            print()
            print("It's a TIE")


    print("\nYour points : ",player_wins)
    print("Computer points : " ,comp_wins)

    user_choice = input("\nDo yoy want to continue the game...(y/n)").lower()
    print("\n================================================")
    if user_choice == "yes" or user_choice == "y":
        pass
    elif user_choice == "no" or user_choice == "n":
        print("Thanks for playing with us !!! ")
        print("<---- Total score of game is follows ---->")
        print("\nYour points : ",player_wins)
        print("Computer points : " ,comp_wins)
        if player_wins>comp_wins:
            print("\nYou are the Winnner & computer Lose ")
        elif comp_wins>player_wins:
            print("\nComputer is the Winner & You Lose ")
        else:
            print("\nGAME TIE")
        break
    else:
        break 
'''
# Default constructor  
'''
class first: # class
    
    def __init__(self): # default constructor
        self.name="kanak"

    def print_name(self): # method
        print("my name is : ",self.name)
        
obj=first() # object creation
obj.print_name() # method calling with object
'''
# Parameterized constructor
'''
class second: # class 

    def __init__(self,age,city): # parameterized constructor 
        self.age=age
        self.city=city

    def print_data(self): # method 
        print("age is : ",self.age)
        print("city is : ",self.city)
        
age=int(input("enter age: "))
city=input("enter city : ")

obj2=second(city=city,age=age) # keyword arguments
obj2.print_data()
'''
# shekhar's cat dog task 
'''
def user():
    user_num=int(input("Enter any 4 digit number : "))
    user_num=str(user_num)
    l=len(user_num)
    if l<4 or l>4:
        print("Entered number is not a four digit number , Try Again ")
        user()
    else:
        print("User Selected : ",user_num)
    return user_num
#user_num=user()

# task
def computer():
    import random
    comp_num=random.randint(1000,9999)
    comp_num=str(comp_num)
    print("computer selected : ",comp_num)
    return comp_num
#comp_num=computer()
a=True
while a:
    user_num=user()
    comp_num=computer()

    k=0
    cats=0
    dogs=0
    for i in range(len(user_num)):
        if comp_num[k] == user_num[k]:
            cats=cats+1
        else:
            dogs=dogs+1 
        k=k+1
        
    print(cats,"cats",end=",")
    print(dogs,"dogs")

    exit_game=input("do you want to quit the game(y/n):")
    if exit_game == "y" or exit_game == "yes":
        print("Thanks for playing with us ")
        break 
    else:
        pass
'''
#
'''
birth_dict={"kanak":"15/06/1999",
                "shekhar":"10/02/1996",
                "sonali":"18/02/1997",
                "rajat":"04/08/2004",
                "ravi":"22/04/1999",
                "lavina":"21/06/1998",
                "minu":"15/07/2001"               
                }
print("Welcome to the birthday Dictionary . we know the birthdays of - ")
for i in birth_dict.keys():
    print(i)
        
print("\nwho's birthday you want to look up ?")
name=input("Enter the name of person here : ")

if name in birth_dict.keys():
    print(name,"birth date is: ",birth_dict.get(name))
else:
    print("sorry...We don't have any data for this name")
'''
#
'''
class myclass:
    def __init__(self,name,a,b):
        self.name=name
        print(a+b)

    def show(self):
        print("name is : ",self.name)

name=input("enter anme : ")
obj1=myclass(name,5,4)
obj1.show()
obj2=myclass("rajat",5,4)
obj2.show()
'''
# constructor overloading 
'''
class first:
    def __init__(self,name):
        self.name=name
        print("name :",self.name)

    def __init__(self,city):
        self.city=city
        print("city :",self.city)
        
ob=first("kanak")
ob2=first("Indore")
'''
#
'''
class A:
    def __init__(self):
        self.name="class A init name"
        self.special="i am special"

class B(A):
    def __init__(self):
        self.name="class B init name"
        super().__init__()

a=A()
b=B()
print(b.name,b.special)
'''
#
'''
class car: # class

    car_wheels=4 # static (class) variable
    
    def __init__(self): # constructor
        
        self.mileage=20 # instance variable
        self.company="maruti suzuki" # instance variable

c1=car() # class instance(onject)
c2=car() # class instance(object)

c2.mileage=10  # updating instance variable value for object 2
c2.company="hyundai" # updating instance variable value for object 2

car.car_wheels=6 # updating class variable value

print(c1.mileage,c1.company,car.car_wheels) # we can access the class(static) variable with the help of class name or object name .
print(c2.mileage,c2.company,car.car_wheels)
'''
#
'''
name_dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,
           "n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

boy_name=input("Enter the name of boy: ").lower()
girl_name=input("Enter the nam eof girl: ").lower()
find_per = "love"


boy_sum=0

for i in boy_name:
    if i in name_dict:
        print(i,":",name_dict.get(i))
        boy_sum=boy_sum+name_dict.get(i)
print("sum of boy's name is: ",boy_sum)


girl_sum=0
for i in girl_name:
    if i in name_dict:
        print(i,":",name_dict.get(i))
        girl_sum=girl_sum+name_dict.get(i)
print("sum of girl's name is: ",girl_sum)


love_sum=0
for i in find_per:
    if i in name_dict:
        print(i,":",name_dict.get(i))
        love_sum=love_sum+name_dict.get(i)
print("sum of love is: ",love_sum)

print("<-------------------------------------------->")

sum_digit_boy=0
while boy_sum>0:
    dig=boy_sum%10
    sum_digit_boy=sum_digit_boy+dig
    boy_sum=boy_sum//10
print("Sum of each digit of boy's name sum is: ",sum_digit_boy)

sum_digit_girl=0
while girl_sum>0:
    dig=girl_sum%10
    sum_digit_girl=sum_digit_girl+dig
    girl_sum=girl_sum//10
print("Sum of all digit of girl's name sum is: ",sum_digit_girl)

print("<---------------------------------------------->")

final_name_sum=sum_digit_boy+sum_digit_girl
print(" Sum of,Sum of each digit of boy & girl name sum is: ",final_name_sum)

print("<---------------------------------------------->")

love_percent=love_sum+final_name_sum
print(boy_name,"&",girl_name,"love percentage is: ",love_percent,"%")
'''
# shekhar's task (Love calculator) with oops
'''
class love_calculator:
    def __init__(self,boy_name,girl_name):
        self.boy_name=boy_name
        self.girl_name=girl_name
        self.find_per="love"
    def show(self):
        name_dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,
           "n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

        boy_sum=0

        for i in boy_name:
            if i in name_dict:
                print(i,":",name_dict.get(i))
                boy_sum=boy_sum+name_dict.get(i)
        print("sum of boy's name is: ",boy_sum)


        girl_sum=0
        for i in girl_name:
            if i in name_dict:
                print(i,":",name_dict.get(i))
                girl_sum=girl_sum+name_dict.get(i)
        print("sum of girl's name is: ",girl_sum)


        love_sum=0
        for i in self.find_per:
            if i in name_dict:
                print(i,":",name_dict.get(i))
                love_sum=love_sum+name_dict.get(i)
        print("sum of love is: ",love_sum)

        print("<-------------------------------------------->")

        sum_digit_boy=0
        while boy_sum>0:
            dig=boy_sum%10
            sum_digit_boy=sum_digit_boy+dig
            boy_sum=boy_sum//10
        print("Sum of each digit of boy's name sum is: ",sum_digit_boy)

        sum_digit_girl=0
        while girl_sum>0:
            dig=girl_sum%10
            sum_digit_girl=sum_digit_girl+dig
            girl_sum=girl_sum//10
        print("Sum of all digit of girl's name sum is: ",sum_digit_girl)

        print("<---------------------------------------------->")

        final_name_sum=sum_digit_boy+sum_digit_girl
        print(" Sum of,Sum of each digit of boy & girl name sum is: ",final_name_sum)

        print("<---------------------------------------------->")

        love_percent=love_sum+final_name_sum
        print(boy_name,"&",girl_name,"love percentage is: ",love_percent,"%")
        
boy_name=input("Enter Boy's name: ").lower()
girl_name=input("Enter girl's name: ").lower()

obj=love_calculator(boy_name,girl_name)
obj.show()
'''
#
'''
class A:
    def __init__(self):
        self.a = 100
        print("A constructor called")
        print(self.a,"in class A")
    def get(self):
        print(self.a)
    
class B(A):
    def __init__(self):
        self.a = 200
        print("B constructor called")
        print(self.a,"in class B")
        super().__init__()
    def get(self):
        print(self.a)
        super().get()
    
b = B()
b.get()
#print(b._dict_) #used to identify the instance of class.
'''
#
'''
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()
 '''
# super keyword with multilevel inheritance
# Derived class inherits features from the base class, adding new features to it. This results into re-usability of code.

'''
class A:
    def __init__(self):
        self.a=100
        print("class A ",self.a)

class B(A):
    def __init__(self):
        self.a=200
        print("class B",self.a)
class C(B):
    def __init__(self):
        self.a=300
        print("class C",self.a)
        super().__init__()
c=C()
'''
# with user input
'''
l=[]
element_num=int(input("Enter how many elemnts you want in your list: "))
for i in range(1,element_num+1):
    ele=input("enter string: ")
    l.append(ele)
print(l)

max_len=0
for i in l:
    length=len(i)
    if length>max_len:
        max_len=length
print(max_len)
final_len=max_len+1

print("* "*(final_len))
for i in l:
    l1=len(i)
    space=final_len-(l1+1)
    print("*",i," "*space," *")

print("* "*final_len)
'''
# without user input
'''
def frame(lst):
    print("Given list is: ",l)
    max_len=0
    for i in l:
        length=len(i)
        if length>max_len:
            max_len=length
    #print(max_len)
    final_len=max_len+1
    print()
    print("* "*(final_len))
    for i in l:
        l1=len(i)
        space=final_len-(l1+1)
        print("*",i," "*space," *")

    print("* "*final_len)
l=["hello","world","in","a","frame"]
frame(l)
'''
# question 3
'''
l=[1,3,4,2,5,6,9,8]
print("The given list is: ",l)
for i in range(1,10):
    if i not in l:
        print("The missing number is: ",i)
'''
# question 4
'''
l=[8,3,8,5,4,3,4,3,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    c=l.count(i)
    if c%2!=0:
        print("odd count is: ",i)
''' 

