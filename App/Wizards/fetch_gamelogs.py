import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/teams/WAS/2024_games.html")

for datum in data:
    print("file saved"
    datum.to_csv(f"Wizards2024.csv")
