import pandas as pd
input = pd.read_csv("../data/data.txt")
grouped = input.groupby('make')
result = grouped.sum().sort(('down'), ascending=False )
print result
result['tonnage'] = result.up.fillna(0) + result.down.fillna(0)
tonnage_sorted = result.sort(('tonnage'), ascending=False )
print tonnage_sorted
