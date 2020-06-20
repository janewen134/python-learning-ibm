import pandas as pd     #为了方便实用pandas 采用pd简写
csv_path='audit_risk.csv'
df=pd.read_csv(csv_path) # use .read_excel() to load excel files
# go over the process to go from a csv file to a data frame
# head can examine the first five rows of a data frame
print(df.head())