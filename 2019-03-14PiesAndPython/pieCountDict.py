import csv

pieListFull = []
pieListFullEdited = []
pieCountDict = {}

# create full list of values from spreadsheet
with open('input.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pie = row['pie']
        pieListFull.append(pie)
print(pieListFull)

# normalize data and create list of edited values
for pie in pieListFull:
    editedPie = pie.lower()
    editedPie = editedPie.replace(' pie', '')
    pieListFullEdited.append(editedPie)

# write csv with a header row
f = csv.writer(open('pieReportDict.csv', 'w'))
f.writerow(['pie'] + ['count'])

# write csv content
for pie in pieListFullEdited:
    pieCount = pieListFullEdited.count(pie)
    pieCountDict[pie] = pieCount
print(pieCountDict)

for pie, pieCount in pieCountDict.items():
    f.writerow([pie] + [pieCount])
