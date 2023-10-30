import pandas as pd


data = pd.read_html("https://www.basketball-reference.com/teams/BOS/2023_games.html")

# print(data.columns.to_list())

count = 0
for datum in data:
    datum.to_csv(f"Boston{count}.csv")
    count+=1