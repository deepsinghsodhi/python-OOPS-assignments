'''
This program asks the user to enter his and his partner name and the program will use logic and calculate 
the love percentage between the entered names.

The logic of Love calculator is basically adapted from the pen and paper games,  and this program is only for fun.

Steps:
Ask user to enter his her : (sam)
Ask user to enter his partner name: (sofi)
According to the alphabets numbering take the sum of user,  his partner name,  and LOVE. (sam = 19 + 1 +13 = 33),  
(sofi = 19 + 15 + 6 + 9 = 49),  (Love = 12 + 15 + 22 + 5 = 54)
Add each digit of the sums individually. (sam = 33 = 3+3= 6 ),  (sofi = 49 = 4+9= 13)
Use the addition operation to Sum of Digits. (6+13 =19)
Sum the Sum of Digit and Love Sum and take (19 + 54 = 73)
Love percentage would be the sum of Love sum and Sum of Digits. (73% for Sam and Sofi)
'''

class Test:
    def __init__(self):
        self.name_dict={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
                "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
        print('*' * 30, "Welcome to The Love Calculator", '*' * 30)
        self.boy_name = input("Enter the name of boy: ").lower()
        self.girl_name = input("Enter the nam eof girl: ").lower()
        self.find_per = "love"


    def calculate(self):
        boy_sum = 0

        for i in self.boy_name:
            if i in self.name_dict:
                # print(i, ":", self.name_dict.get(i))
                boy_sum = boy_sum + self.name_dict.get(i)
        print("sum of boy's name is: ", boy_sum)


        girl_sum = 0
        for i in self.girl_name:
            if i in self.name_dict:
                # print(i, ":", self.name_dict.get(i))
                girl_sum = girl_sum + self.name_dict.get(i)
        print("sum of girl's name is: ", girl_sum)


        love_sum = 0
        for i in self.find_per:
            if i in self.name_dict:
                # print(i, ":", self.name_dict.get(i))
                love_sum = love_sum + self.name_dict.get(i)
        print("sum of love is: ", love_sum)

        print("<-------------------------------------------->")

        sum_digit_boy = 0
        while boy_sum>0:
            dig = boy_sum % 10
            sum_digit_boy = sum_digit_boy + dig
            boy_sum = boy_sum//10
        print("Sum of each digit of boy's name sum is: ", sum_digit_boy)

        sum_digit_girl = 0
        while girl_sum>0:
            dig = girl_sum % 10
            sum_digit_girl = sum_digit_girl + dig
            girl_sum = girl_sum//10
        print("Sum of all digit of girl's name sum is: ", sum_digit_girl)

        print("<---------------------------------------------->")

        final_name_sum = sum_digit_boy + sum_digit_girl
        print(" Sum of, Sum of each digit of boy & girl name sum is: ", final_name_sum)

        print("<---------------------------------------------->")

        love_percent = love_sum + final_name_sum
        print(self.boy_name, "&", self.girl_name, "love percentage is: ", love_percent, " % ")

t = Test()
t.calculate()