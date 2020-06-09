#balance brackets program
str1 = input("Enter square brackets:")      # string to check the program
check = ["[]", "()", "{}"]                  # Through the program we check types of bracket which are present in list

while any(i in str1 for i in check):        # if any complete bracket present in str1 then it is replaced by empty space
    for j in check:
        str1 = str1.replace(j, '')

if len(str1) == 0:                          # Finally if len of str1 is 0 then the brackets are balanced
    print("OK(balanced)")
else:
    print("NOT OK(unbalanced)")             # else not balanced