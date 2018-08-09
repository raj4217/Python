import csv

using normal writer
with open('input.csv', 'r') as rf:
    rcsv = csv.reader(rf)
    with open('output1.csv', 'w', newline='')as wf:
        wcsv = csv.writer(wf, delimiter=',')
        for i in rcsv:
            wcsv.writerow(i[:2])


# using Dictwriter

with open('input.csv') as rf:
    rcsv = csv.DictReader(rf)
    with open('output2.csv', 'w', newline='') as wf:
        header = ['first_name', 'last_name']
        wcsv = csv.DictWriter(wf, fieldnames=header, delimiter=',')
        for line in rcsv:
            del line['email']
            wcsv.writerow(line)
