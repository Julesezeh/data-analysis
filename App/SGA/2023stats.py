import pandas as pd

data = pd.read_csv("shai7.csv")

three_point_shooting_data = data.loc[:,["Date","PTS","3PA","3P","Opp"]]
fg_data = data.loc[:,["Date","PTS","FGA","FG","Opp"]]
# rebound_data = data.loc[:,["Opp","TRB"]]

# print(shooting_data["3PM"].max)



print(data.columns.to_list())
#Getting for specific opponents
try:
    opps = input("Opposition?:").upper()

    print(three_point_shooting_data.loc[three_point_shooting_data["Opp"]==opps])
    print("\n\n\n")
    print(fg_data.loc[fg_data["Opp"]==opps])

except:
    print("Invalid team")
