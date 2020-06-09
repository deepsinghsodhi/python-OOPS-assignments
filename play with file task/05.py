'''
5) Write a function to print the count no. of sentences in a text file STORY.TXT.
for example, if the content of the file STORY.TXT is
There was a monkey in the zoo. The monkey was very naughty.
Then the ouput of the program should be 2

'''

'''
def Writing(): # writing a STORY txt file
    with open("STORY.txt", "w") as fw:
        string = "There was a monkey in the zoo. The monkey was very naughty."
        writing_file = fw.write(string)
        
Writing()

'''
def Reading(): # Reading a STORY txt file
    with open("STORY.txt", "r") as fr:
        Reading_file = fr.read()
        line_list = list(Reading_file.split(". ")) # spliting the lines according to the fullstop. 
        print(line_list,"Having", len(line_list), "Lines.")
        
Reading()
