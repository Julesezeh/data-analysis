import pandas as pd

url = "https://www.basketball-reference.com/teams/BOS/2024_games.html"

data = pd.read_html(url)

# print(data.columns.to_list())

count = 0
for datum in data:
    datum.to_csv(f"Boston_recent_{count}.csv")
    count+=1