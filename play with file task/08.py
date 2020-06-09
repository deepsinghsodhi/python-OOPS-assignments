'''
8) Assuming that a text file named FIRST.TXT contains some text written into it, 
write a function named vowelwords(), that reads the file FIRST.TXT and creates a new 
file named SECOND.TXT, to contain only those words from the file FIRST.TXT which start 
with a lowercase vowel (i.e., with 'a', 'e', 'i', 'o', 'u').
For example, if the file FIRST.TXT contains
Carry umbrella and overcoat when it rains
Then the file SECOND.TXT shall contain
umbrella and overcoat it solution
'''
# Writing a FIRST1 txt file.
'''
def Writing(): 
    with open("FIRST1.txt", "w") as fw:
        string = "Carry umbrella and overcoat when it rains.\nAll are in lower case.\nThe rose is red.\nA girl is playing there.\nThere is a playground.\nAn aeroplane is in the sky.\nNumbers are not allowed in the password."
        writing_file = fw.write(string)
Writing()
'''
class VowelWords:
    def Reading(self): # Method for reading FIRST1.txt file.
        # reading file from FIRST1.txt file.
        with open("FIRST1.txt", "r") as fr:
            self.Reading_file = fr.read()
            print(self.Reading_file, "\n -----------------------------------")
        self.Writing()

    # method to writing "SECOND.txt" file after reading FIRST.txt file.
    def Writing(self):
        with open("SECOND1.txt", "w") as fw:
            word_list = list(self.Reading_file.split(" "))
            vowel_list = ['a', 'e', 'i', 'o', 'u']  # This list check for the first latter of word is vowel.
            vowel_word_list = []
            vowel_word_string = "" 
            for word in word_list:
                if word[0] in vowel_list:
                    vowel_word_list.append(word)
                    vowel_word_string += str(word) + " "
                else:
                    pass
            vowel_words = fw.write(vowel_word_string) # Writing vowel words into the SECOND1.txt file.
        self.ReadingVowelWords()

    # Method to Read or print Vowel Words on the shell.
    def ReadingVowelWords(self):
        with open("SECOND1.txt", "r") as fr:
            self.Reading_file = fr.read()
            print("Extracted Vowel Words from above lines:-", self.Reading_file)

v = VowelWords()
v.Reading()