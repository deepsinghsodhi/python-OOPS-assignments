import csv

class a:
    def Show(self):
        with open('input.csv') as f:
            csv_reader = csv.reader(f, delimiter=',')

        for l in csv_reader:
            if line == 0:
                print(f'column names are {l}')
                line += 1
            else:
                print(f'\n {l[0]} {l[1]} {l[2]} {l[3]}')
                line += 1

    print(f'Total lines are {line}')

with open('output.csv',mode='w') as f1:
    line = 0
    csv_writer = csv.writer(f1, delimiter= ',')
    for row in csv_reader:
        if line == 0:
            row.extend(['Tax', 'Total'])
            csv_writer.writerow(row)
            line+=1
        else:
            if 'India' in row:
                total = float(row[2]) + float(row[2]) * 0.05
                row.extend(['5%', total])
                csv_writer.writerow(row)
            if 'Japan' in row:
                total = float(row[2]) + float(row[2]) * 0.1
                row.extend(['10%', total])
                csv_writer.writerow(row)
            if 'Egypt' in row:
                total = float(row[2]) + float(row[2]) * 0.15
                row.extend(['15%', total])
                csv_writer.writerow(row)