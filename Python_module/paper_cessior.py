user_points = 0
computer_points = 0

print("=========== Rock paper & Scissors game ===========")

print(" \nOptions available for the user to choose from \n\n 1 -> Rock\n 2 -> Paper\n 3 -> Scissor")

print("\n Winning combinations are follows:")

print("\n Rock Vs Rock = Tie")
print(" Rock Vs Paper = paper won")
print(" Rock Vs Scissors = Rock won")

print("\n Paper Vs Rock = paper won")
print(" Paper Vs Paper = Tie")
print(" Paper Vs Scissors = scissor won")

print("\n Scissors Vs Rock = Rock won")
print(" Scissors Vs Paper = Scissor won")
print(" Scissors Vs Scissors = Tie")

print("===================================================================================================== ")

print("\n This is your turn")

def game():
    user_points = 0
    computer_points = 0
    
    user_choice = int(input("\n Enter your choice (in number): "))
    if user_choice == 1:
        user_choice_name = "rock"
    elif user_choice == 2:
        user_choice_name = "paper"
    elif user_choice == 3:
        user_choice_name = "scissor"
    else:
        print("you entered some invalid choice")
    print("\n Your choice is: ", user_choice_name)

    import random
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_name = "rock"
    elif computer_choice == 2:
        computer_choice_name = "paper"
    elif computer_choice == 3:
        computer_choice_name = "scissor"
    else:
        print("you entered an invalid choice")

    print("\n This is computer's turn")
    print("\n Computer's choice is: ", computer_choice_name)

    print("\n=====================================")
    print("\n", user_choice_name, " VS ", computer_choice_name)
    print("\n================================")


    if user_choice == 1:
        if computer_choice == 1:
            print("\n It's a TIE, both players selected same choice")
        elif computer_choice == 2:
            computer_points = computer_points + 1
            print("\n paper won -> computer won")
        elif computer_choice == 3:
            user_points = user_points + 1
            print("\n scissor won -> you won")

    if user_choice == 2:
        if computer_choice == 1:
            user_points = user_points + 1
            print("\n Paper won -> you won")
        elif computer_choice == 2:
            print("\n It's a TIE, both players selected same choice ")
        elif computer_choice == 3:
            computer_points = computer_points + 1
            print("\n scissor won -> computer won ")

    if user_choice == 3:
        if computer_choice == 1:
            computer_points = computer_points + 1
            print("\n Rock won -> computer won")
        elif computer_choice == 2:
            user_points = user_points + 1
            print("\n Scissor won -> user won")
        elif computer_choice == 3:
            print("\n It's a TIE, both players selected same choice ")

    print(" user score is: ", user_points)
    print(" computer's score is: ", computer_points)

    print("\n===============================")

    print("\n Do you want to continue the game (Y/N)")
    cont = input("\n Enter yes or no: ")
    if cont == "yes" or cont == "Y" or cont == "Yes" or cont == "y" or cont == "YES":
        game()
    elif cont == "no" or cont == "N" or cont == "No" or cont == "n" or cont == "NO":
        print(" Thanks for playing with us")
 
game()