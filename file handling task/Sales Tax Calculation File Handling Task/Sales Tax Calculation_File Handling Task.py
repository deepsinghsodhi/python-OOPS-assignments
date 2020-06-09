import csv
with open('input.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
   
    for line in csv_reader:
        if line == 0:
            print(f'column names are {line}')
            line += 1
        else:
            print(f'\n {line[0]} {line[1]} {line[2]} {line[3]}')
            line += 1

    print(f'Total lines are {line}')
    
    with open('outdata.csv',mode='w') as f1:
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
                    row.extend(['50%', total])
                    csv_writer.writerow(row)
                if 'Japan' in row:
                    total = float(row[2]) + float(row[2]) * 0.1
                    row.extend(['30%', total])
                    csv_writer.writerow(row)
                if 'Egypt' in row:
                    total = float(row[2]) + float(row[2]) * 0.15
                    row.extend(['20%', total])
                    csv_writer.writerow(row)
                    