import pandas as pd
df = pd.read_csv("kdrama_DATASET.csv", encoding="utf-8")
# print(df)
df1 = pd.read_excel("Historicalinvesttemp.xlsx")
# print(df1)
df2 = pd.read_json("titanic.json", lines=True)
print(df2)