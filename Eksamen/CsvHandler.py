import csv

def insertRow(filename, list, delimeter):
    csv.register_dialect("custom", delimiter=delimeter)
    with open(filename+'.csv', 'a') as f:
        writer = csv.writer(f, dialect="custom")
        writer.writerow(list)

def deleteRow(filename, rowIndex):
    lines = list()
    i = 0
    
    with open(filename + '.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for rows in reader:
            if i == rowIndex:
                pass
            else:
                lines.append(rows)
            i+=1

    if rowIndex == -1:
        del lines[-1]

    with open(filename + '.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

def getRow(filename, rowIndex):
    with open(filename + '.csv','r') as readfile:
        reader=csv.reader(readfile)
        rows=[r for r in reader]
    return rows[rowIndex]

def printAll(filename, delimeter):
    with open(filename + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimeter)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)}')
                line_count += 1
            else:
                print(f'{row}')
                line_count += 1