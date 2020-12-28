import pandas as pd

""" df = pd.DataFrame(columns=["DateTime", "Number"])
df.to_csv("document.csv", index=False) """

df = pd.read_csv("document.csv", )
print(df)