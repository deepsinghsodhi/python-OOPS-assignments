'''
Write a function to count and display the number of lines not starting with alphabet 'A' present in a text file "STORY.TXT".
Example:
If the file "STORY.TXT" contains the following lines,
The rose is red.
A girl is playing there.
There is a playground.
An aeroplane is in the sky.
Numbers are not allowed in the password.

The function should display the output as 3

'''

'''
def Writing(): # writing a STORY txt file
    with open("STORY1.txt", "w") as fw:
        story = "The rose is red.\nA girl is playing there.\nThere is a playground.\nAn aeroplane is in the sky.\nNumbers are not allowed in the password."
        writing_file = fw.write(story)
Writing()
'''

def Reading(): # Reading a STORY txt file
    with open("STORY1.txt", "r") as fr:
        Reading_file = fr.read()
        line_list = list(Reading_file.split("\n")) # spliting the lines according to the fullstop. 
        count = 0
        lines = []
        for line in line_list:
            if line[0] == "A":
                pass
            else:
                lines.append(line)
                count += 1
        print("There are", count, "lines which are not started with 'A'.")
Reading()
