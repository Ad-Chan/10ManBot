import csv


f = open('users.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print(row)
