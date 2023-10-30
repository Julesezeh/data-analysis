import pandas as pd

data = pd.read_csv("shaiRecent.csv")

three_point_shooting_data = data.loc[:,["Date","PTS","3PA","3P","Opp"]]
fg_data = data.loc[:,["Date","PTS","FGA","FG","Opp"]]


print(three_point_shooting_data)