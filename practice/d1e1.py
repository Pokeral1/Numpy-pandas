import csv
import statistics
with open('practice/d1e1.csv','r') as file:
    reader=csv.DictReader(file)
    names=[]
    score=[]
    for row in reader:
        print(row['name'],row['score'])
        names.append(row['name'])
        score.append(int(row['score']))
    print("Average = ",(sum(score)/len(score)))
    high=max(score)
    high_name=names[score.index(high)]
    low=min(score)
    low_name=names[score.index(low)]
    print(f"Highest = {high} obtained by {high_name}")
    print(f"Lowest = {low} obtained by {low_name}")
    print(f"Median = {statistics.median(score)}")
    print(f"Range = {high-low}")
    stdev = statistics.stdev(score)
    print(f"Standard Deviation = {stdev}")
    print(f"Consistency = {'Consistent' if stdev < 15 else 'Varied'}")