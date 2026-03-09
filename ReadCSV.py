import csv
import statistics
with open('c1.csv','r') as file:
    reader = csv.DictReader(file)  # reads each row as a dictionary
    for row in reader:
        print(row)
