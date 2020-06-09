'''
4)Write a function to count number of words in a text file named "OUT.TXT"
'''
def Reading():
    with open("OUT.txt", "r") as fr:
        Reading_file = fr.read()
        Name_list = list(Reading_file.split(" "))
        Words_only = []
        for word in Name_list:
            if word == " ":
                pass
            else:
                Words_only.append(word)
        num_words = len(Words_only)
        print(f'There are "{num_words}" words are present in "{Reading_file}" string.')
Reading()