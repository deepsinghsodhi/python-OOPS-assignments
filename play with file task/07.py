'''
7) Assuming that a text file named FIRST.TXT contains some text written into it, 
write a function named copyupper(), that reads the file FIRST.TXT and creates a 
new file named SECOND.TXT contains all words from the file FIRST.TXT in uppercase.
'''
'''
def Writing(): # writing a FIRST txt file having lower case fonts.
    with open("FIRST.txt", "w") as fw:
        lower_case = "All are in lower case.\nThe rose is red.\nA girl is playing there.\nThere is a playground.\nAn aeroplane is in the sky.\nNumbers are not allowed in the password."
        writing_file = fw.write(lower_case.lower())
Writing()
'''
class UpperCase:
    def LowerCase_Reading(self): # Method for reading lower case from FIRST.txt file.
        # reading file from FIRST.txt file which are in Lower case.
        with open("FIRST.txt", "r") as fr:
            self.Reading_file = fr.read()
            print(self.Reading_file, "\n")
        self.UpperCase_Reading()

        # method to writing UpperCase "SECOND.txt" file after reading lowerCase (FIRST.txt) file.
    def UpperCase_Reading(self):
        with open("SECOND.txt", "w") as fw:
            writing_upper_case = fw.write(self.Reading_file.upper())
        self.Reading_Upper_case()

        # Reading UpperCase file (SECOND.txt) 
    def Reading_Upper_case(self):
        with open("SECOND.txt", "r") as fr:
            self.Reading_file = fr.read()
            print(self.Reading_file.upper())

upper = UpperCase()
upper.LowerCase_Reading()

  