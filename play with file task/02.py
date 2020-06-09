'''
2)Write a user-defined function to read the content from a text file OUT.TXT, 
count and display the number of alphabets present in it.(exclude white spaces and special char)
'''
def Reading():       #
    with open("OUT.txt", "r") as fr:
        Reading_file = fr.read()
        alphanum = ""       # It will hold only the alphabets.
        for chr in Reading_file:
            if chr.isalnum(): 
                alphanum += chr
            else:
                pass
        print(f'There are "{(len(alphanum))}" number of alphabets are present in "{Reading_file}" string.')

Reading()