import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/WorkAccount/Desktop/Programming/ST2187/ST2187_coursework_project/st2187_coursework_dataset_2022 (1).xlsx')
print(df.head())

print(df['Order Date'].count().sum())
print(df.loc[df['Ship Date'].astype(str).str.contains('2020'), 
       'Category'].count())

search_values = ['2017', '2018', '2019', '2020']

counts = {val: 0 for val in search_values}

for val in df['Ship Date']:
    for search_val in search_values:
        if search_val in str(val):
            counts[search_val] += 1

for search_val, count in counts.items():
    print(f"{search_val}: {count}")

    

