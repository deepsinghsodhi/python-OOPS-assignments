'''
2)Write a program that generates a random number and asks the user to guess what the number is. 
If the user's guess is higher than the random number, the program should display "Too high, try again." 
If the user's guess is lower than the random number, the program should display "Too low, try again." 
The program should use a loop that repeats until the user correctly guesses the random number.
'''
# ================================================================================================================================

import random as rn
class RandomNum:                    
    def NumGenerator(self):             # Method to generate a random number.
        self.Gen_number = rn.randint(0,9)
        self.NUmGuess()

    def NUmGuess(self):                 # Method to take guessed one digit number.
        self.guessnum = int(input("Guess, What should be that one Digit Number:"))
        self.Result()

    def Result(self):
        condition = False
        while not condition:                
            if self.guessnum < self.Gen_number:         # if guessed number is lower.
                print("Number is Lower then the Generated Number, Please Try again!")
                self.NUmGuess()
            elif self.guessnum > self.Gen_number: # IF guessed number is higher.
                print("Number is Higher then the Generated Number, Please Try again!")
                self.NUmGuess()
            else:
                print("Correct guessed Number!!!")
            condition = True  #when the user guesses the correct number, this condtion breaks the loop.

r = RandomNum()
r.NumGenerator()