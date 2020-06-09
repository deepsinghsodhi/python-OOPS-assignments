'''
1)Write a program, which initializes a string variable to the content "Time is a great teacher but 
unfortunately it kills all its pupils. Berlioz" and outputs the string to the disk file OUT.TXT
'''

def Writing(): # writing a txt file
    with open("OUT.txt", "w") as fw:
        string = "Time is a great teacher but unfortunately it kills all its pupils. Berlioz"
        writing_file = fw.write(string)
Writing()

