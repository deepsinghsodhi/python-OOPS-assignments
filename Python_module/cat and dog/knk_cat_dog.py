def user():
    user_num = int(input("Enter any 4 digit number : "))
    user_num = str(user_num)
    l = len(user_num)
    if l < 4 or l > 4:
        print("Entered number is not a four digit number! Please Try Again ")
        user()
    else:
        print("User Selected : ", user_num)
    return user_num
user_num = user()

# task
def computer():
    import random
    comp_num = random.randint(1000, 9999)
    comp_num = str(comp_num)
    print("Computer's Digits : ", comp_num)
    return comp_num

comp_num = computer()

k = 0
condition = True
while condition:
    for i in comp_num:
        if i is user_num[k]:
            print("cats", end = " ")
            k = k+1
        else:
            print("dogs", end = " ")
            k = k+1
    
    option = input("\nPress 'e' to Exit the game and 'c' to continue: ")
    if option == "E" or option == "e":
        condition = False
        break   
    else:
        again1 = computer()
        again = user()