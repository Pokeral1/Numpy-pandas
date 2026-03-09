import csv
data=[
    {'Name':'Burger','Price':'69','Quantity':'10'},
    {'Name':'Pasta','Price':'119','Quantity':'4'},
    {'Name':'Pizza','Price':'199','Quantity':'6'}
]
with open ('practice/d1e3.csv','w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=['Name','Price','Quantity'])
    writer.writeheader()
    writer.writerows(data)
