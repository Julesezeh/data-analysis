import pandas as pd

data = pd.read_csv("Tatum2023.csv")

# print(data)
data.rename(
    columns={"Unnamed: 5":"Home/Away" },
    inplace=True
    )

shooting_data = (data.loc[:,["Opp","3P","3PA","Home/Away"]])

opps = input("Opp? >")

print(shooting_data.loc[shooting_data["Opp"] == opps])





