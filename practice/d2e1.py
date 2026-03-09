import csv
import statistics
def load_csv(filepath):
    with open (filepath,'r') as file:
        reader=csv.DictReader(file)
        name=[]
        score=[]
        for row in reader:
            name.append(row['name'])
            score.append(int(row['score']))
    return name,score
def get_stats(names, scores):
    stdev=statistics.stdev(scores)
    high=max(scores)
    low=min(scores)
    return{
    'Average marks':sum(scores)/len(scores),
    'Highest marks': high,
    'Highest scorer':names[scores.index(high)],
    'Lowest marks':low,
    'Lowest scorer':names[scores.index(low)],
    'median':statistics.median(scores),
    'stdev': round(stdev, 2),
    'consistency': 'Consistent' if stdev < 15 else 'Varied'
    }
names,scores=load_csv('students.csv')
print(names)
print(scores)
stats=get_stats(names,scores)
for key, value in stats.items():
    print(f"{key}: {value}")