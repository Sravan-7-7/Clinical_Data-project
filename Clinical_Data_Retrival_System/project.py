import pandas as pd

df = pd.read_csv('Clinical_Data.csv', index_col='Name')

patient = input('Enter patient Name: ').title()

try:
    print(df.loc[patient])
except KeyError:
    print(f'{patient} not found')