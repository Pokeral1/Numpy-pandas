import pandas as pd
data={
    'product':["Pens","Pencils","Notebook","Registers"],
    'price':[50,5,30,60],
    'stock':[100,500,200,50]
    
}
df=pd.DataFrame(data)
print(df)
print(df['price'])