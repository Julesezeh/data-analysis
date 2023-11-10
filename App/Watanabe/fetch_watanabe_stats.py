import pandas as pd


data = pd.read_html("https://www.basketball-reference.com/players/w/watanyu01/gamelog/2023")

count = 0 
for datum in data:
    datum.to_csv(f"Watanabe{count}")
    count+=1