import csv
from fuzzywuzzy import fuzz

pieListFull = []

#create full list of values from spreadsheet
with open('input.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pie = row['pie']
        editedPie = pie.lower().replace(' pie', '')
        pieListFull.append(editedPie)
print(pieListFull)

completeNearMatches = []
for pie in pieListFull:
    for pie2 in pieListFull:
        if pie != pie2:
            ratio = fuzz.ratio(pie, pie2)
            partialRatio = fuzz.partial_ratio(pie, pie2)
            tokenSort = fuzz.token_sort_ratio(pie, pie2)
            tokenSet = fuzz.token_set_ratio(pie, pie2)
            avg = (ratio+partialRatio+tokenSort+tokenSet)/4
            if avg > 70:
                nearMatch = [str(avg), pie, pie2]
                nearMatch = sorted(nearMatch)
                if nearMatch not in completeNearMatches:
                    completeNearMatches.append(nearMatch)
        else:
            pass

#write csv of near matches
f=csv.writer(open('pieNearMatches.csv', 'w'))
f.writerow(['matchPercentage']+['pie1']+['pie2'])
for nearMatch in completeNearMatches:
    f.writerow([nearMatch[0]]+[nearMatch[1]]+[nearMatch[2]])
