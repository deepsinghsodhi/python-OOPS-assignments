'''
1) Write a python program to create / write a CSV file that store name, DOB of minimum 10 friends on
separated lines by taking user input

2) we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
Create a dictionary of names and birthdays(by reading the csv file). When you run your program it should 
display all the friends name and ask the user to enter a name, and return the birthday of that person back 
to them. The interaction should look something like this:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert
Einstein
Benjamin
Franklin
Ada
Lovelace
john
...
>>> Who's birthday do you want to look up?
Franklin
>>> Franklin's birthday is 01/17/1706.
'''
# ====================================================================
import csv
'''
# Writing CSV file
with open("DOB.csv", "w", newline='') as f:
    csv_writer = csv.writer(f, delimiter = ',')
    csv_writer.writerow(["Name", "DOB"])

    for i in range(5):
        Name = input("Enter friend's name: ")
        DOB = input("Enter Date OF Birth: ")
        csv_writer.writerow([Name, DOB])
'''
# ====================================================================

# Reading a csv file
with open("DOB.csv", 'r') as f:
    csv_reader = csv.DictReader(f)
        
    for i in csv_reader:
        for j in csv_reader:
            print(j["Name"])

        fname = input(" Who's birthday do you want to look up?")
        print(f"{fname}'s birthday is", i['DOB'])
