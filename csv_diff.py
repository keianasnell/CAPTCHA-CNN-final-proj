import pandas as pd
import difflib as diff


df = pd.read_csv('last_test.csv')
#Create a new column 'diff' and get the result of comparision to it
df['diff'] = df.apply(lambda x: diff.SequenceMatcher(None, x[0].strip(), x[1].strip()).ratio(), axis=1) 
#Save the dataframe to CSV and you could also save it in other formats like excel, html etc
df.to_csv('outdata.csv',index=False)