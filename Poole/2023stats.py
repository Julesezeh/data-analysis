import pandas as pd

data = pd.read_csv("poole7.csv")

# print(data)
shooting_data = (data.loc[:,["Opp","3P","3PA"]])

opps = input("Opp? >")

print(shooting_data.loc[shooting_data["Opp"] == opps])
