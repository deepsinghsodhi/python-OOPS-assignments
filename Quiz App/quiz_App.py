'''
WAP in that display question (like MCQ) with 4 options(A,B,C,D) on screen 
and ask for user to enter correct option, if user enter the correct option 
then its score increase by one ,
Your program should ask at least five question.

Genrally this task related to Database but think how you can do without using DB.

e.g
What is capital of India?
A. Mumbai
B. Delhi
C. Pune
D. Banglore
Enter your option: B
...
...
...
Total Question:5
Correct Answer:3
Incorrect Answer:2

<In this way its ask 5 questions and at last display the score>
'''
# ================================================================================================================

class Quiz:
    total_que = 0
    correct = 0
    incorrect = 0

    def __init__(self):
        print("\t\t ----Welcome to Python Quiz----")
        self.Q1()
    def Q1(self):   #<<< Question no.1
        print("1) Python is _______ language.")
        print("A. Assembly. \nB. Interpreted. \nC. Compiled. \nD. None of These")
        q1 = input("Enter Your Answer: ")
        Quiz.total_que += 1
        if q1 == "B" or q1 == "b":
            Quiz.correct += 1
        else:
            Quiz.incorrect += 1
        self.Q2()
    
    def Q2(self): #<<< Question no.2
        print("\n2) Number of keywords in Python.")
        print("A. 32. \nB. 43. \nC. 33. \nD. 35")
        q2 = input("Enter Your Answer: ")
        Quiz.total_que += 1
        if q2 == "C" or q2 == "c":
            Quiz.correct += 1
        else:
            Quiz.incorrect += 1    
        self.Q3()

    def Q3(self):       #<<< Question no.3
        print("\n3) Which of the following is not a Framework of Python.")
        print("A. Django. \nB. Pyramid. \nC. Drupal. \nD. Flask")
        q3 = input("Enter Your Answer: ")
        Quiz.total_que += 1
        if q3 == "C" or q3 == "c":
            Quiz.correct += 1
        else:
            Quiz.incorrect += 1    
        self.Q4()

    def Q4(self):       #<<< Question no.4
        print("\n4) Who Created Python ?")
        print("A. James Gosling. \nB. Denis Ritchie. \nC. Tom Cruise. \nD. Guido Van Rossum")
        q4 = input("Enter Your Answer: ")
        Quiz.total_que += 1
        if q4 == "D" or q4 == "d":
            Quiz.correct += 1
        else:
            Quiz.incorrect += 1 
        self.Q5()

    def Q5(self):          #<<< Question no.5
        print("\n5) In Python, Which Keywor is used to start a Function ?")
        print("A. function. \nB. try. \nC. def. \nD. import")
        q5 = input("Enter Your Answer: ")
        Quiz.total_que += 1
        if q5 == "C" or q5 == "c":
            Quiz.correct += 1
        else:
            Quiz.incorrect += 1
        self.Result()

    def Result(self):           #This method will show the Overall Result.
        print("-*-"*5, "Your Result", "-*-"*5)
        print("Total Questions:", Quiz.total_que)
        print("Correct Answers:", Quiz.correct)
        print("Incorrect Answers:", Quiz.incorrect)

q = Quiz()

