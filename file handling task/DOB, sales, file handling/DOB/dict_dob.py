# dict writing

import csv

'''
# Writing a csv file in dict form
class Write:
    def Write_csv(self):
        with open("Find_dob.csv", 'w', newline='') as fd:
            fieldnames = ["Name", "DOB"]
            dict_write = csv.DictWriter(fd, fieldnames = fieldnames, delimiter = ",")
            dict_write.writeheader()

            for i in range(5):
                fname = input("Enter friend's Name:")
                fdob = input("Enter Friend's DOB:")
                dict_write.writerow({"Name":fname, "DOB":fdob})
    
w = Write()
w.Write_csv()
'''
# Reading a csv dict file
class Read:
    def Read_csv(self):
        with open("Find_dob.csv", 'r') as f:
            dict_read = csv.DictReader(f)
            for i in dict_read:
                print(i['Name'])
            f.seek(0)
            fname = input("Who's birthday do you want to look up?:")
            for i in dict_read:
                if fname == i['Name']:
                    print(f"{fname}'s birthday is on", i['DOB'])    
r = Read()
r.Read_csv()
