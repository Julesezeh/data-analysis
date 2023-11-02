import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/teams/WAS/2023_games.html")

count = 0
for datum in data:
    datum.to_csv(f"Wizards{count}")