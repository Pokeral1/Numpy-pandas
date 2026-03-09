import csv
data=[
    {'Name': 'Rahul', 'Designation': ' Employee', 'Age': '34', 'ID': '001', 'Salary': '25000'},
{'Name': 'Rohit', 'Designation': ' Employee', 'Age': '29', 'ID': '002', 'Salary': '31000'}
]
with open('c2.csv','w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=['Name','Designation','Age','ID','Salary'])
    writer.writeheader()
    writer.writerows(data)