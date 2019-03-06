import csv

pieListFull = []
pieListFullEdited = []
pieListUnique = []

# create full list of values from spreadsheet
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        pie = row[1]
        pieListFull.append(pie)
print(pieListFull)

# normalize data and create list of edited values
for pie in pieListFull:
    editedPie = pie.lower()
    editedPie = editedPie.replace(' pie', '')
    pieListFullEdited.append(editedPie)

# write csv with a header row
f = csv.writer(open('pieReportLists.csv', 'w'))
f.writerow(['pie'] + ['count'])

# create list of unique values
for editedPie in pieListFullEdited:
    if editedPie not in pieListUnique:
        pieListUnique.append(editedPie)
    else:
        pass
print(pieListUnique)

# write csv content
for pie in pieListUnique:
    pieCount = pieListFullEdited.count(pie)
    f.writerow([pie] + [pieCount])
