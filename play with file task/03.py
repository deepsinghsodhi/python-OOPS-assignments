'''
3)Write a function to count the number of blank present in a text file named "OUT.TXT"
'''
def Reading():
    with open("OUT.txt", "r") as fr:
        Reading_file = fr.read()
        # print(Reading_file)
        white_spaces = 0
        for chr in Reading_file:
            if chr == " ":
                white_spaces += 1
        print(f'There are "{(white_spaces)}" number of White spaces are present in "{Reading_file}" string.')
        
Reading()