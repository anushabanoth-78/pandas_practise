import pandas as pd
data = {
     'names' :['anusha','manohar','rishi'],
     'rollnumber':[1,2,3,],
     'class':['1st','2nd','3rd']
 }
 
df = pd.DataFrame(data)
print(df)