# seperate the string and digit which are also string in a list.

lst=["10","ten","20","twenty","30"]
print(lst)
print(type(lst))
digit_lst = []
alpha_lst = []
for i in lst:
    if i.isdigit():
        digit_lst.append(i)
    elif i.isalpha():
        alpha_lst.append(i)
    else:
        print("symbol")
        
#print(digit_lst)
print(type(digit_lst))

final_list=list(map(lambda x:int(x) , digit_lst))
print(final_list)
print(type(final_list))

for i in final_list:
    print(i,type(i))