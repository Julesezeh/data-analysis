import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/players/p/poolejo01/gamelog/2023")

number = 0
for datum in data:
    datum.to_csv(f"poole{number}.csv")
    number +=1