'''
2) Write a program which Calculate Income Tax of an employee. The program should
calculate the income tax to be paid by the employee as per the criteria given below:

IT.csv
---------
Slab rate, IT rate
Upto Rs.50000,Nil
Upto Rs.60000, 10% on additional amount
Upto Rs.150000,20% on additional amount
Above Rs.150000,30% on additional amount
------------
Read from csv file and calculate tax amount

Input: - Enter employee name and income: Ajay 1,25,000
Output: -Hello Ajay, your income tax is …………………………….
================================================X================================================
'''

import csv
'''
                        #writing a file
with open("It.csv",mode='w',newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(['Slab Rate', 'IT rate'])
    csv_writer.writerow(['Upto Rs50000','Nil'])
    csv_writer.writerow(['Upto Rs60000','10% on additional amount'])
    csv_writer.writerow(['Upto Rs150000', '20% on additional amount'])
    csv_writer.writerow(['Above Rs150000', '30% on additional amount'])
'''
input1 = input("Enter Employee name and income:")
k = input1.split(" ")
income = int(k[1])
#print(income)
                        #reading a file
with open("It.csv", mode='r') as f1:
    amount =0
    csv_reader = csv.reader(f1, delimiter = ',')
    next(csv_reader)
    line_count = 0
    for line in csv_reader:
        if income <= 50000 and line_count == 0 :
            print(f'Hello {k[0]}, your income tax is {line[1]}')
            line_count += 1
            break
        else:
            if income > 50000 and income <= 60000 and line_count == 1:
                q = str(line[1]).split("%")
                tax_per =int(q[0])
                amount = amount + (income - 50000) * (tax_per / 100)
                print(f'Hello {k[0]}, your income tax is Rs {amount}')
                break
            elif income > 60000 and income <= 150000 and line_count == 2:
                q = str(line[1]).split("%")
                tax_per = int(q[0])
                amount = amount + (income - 60000) * (tax_per / 100)
                print(f'Hello {k[0]}, your income tax is Rs {amount}')
                break
            elif income > 150000 and line_count == 3:
                q = str(line[1]).split("%")
                tax_per = int(q[0])
                amount = amount + (income - 150000) * (tax_per / 100)
                print(f'Hello {k[0]}, your income tax is Rs {amount}')
                break
            line_count += 1

