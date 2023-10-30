import pandas as pd

data = pd.read_csv("tatum7.csv")

# shooting_data = data[["3P","3PA","Date"]]
shooting_data = data.loc[:,["Opp","3P","3PA"]]

print(shooting_data.loc[shooting_data["Opp"] =="DAL"])
# print(data.columns.to_list())
