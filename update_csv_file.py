import pandas as pd


df = pd.read_csv("result.csv", names=['Doctor', 'Work time', 'Address', 'Rating'])
df.to_csv("new.csv", index=False)

