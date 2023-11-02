import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/players/d/duranke01/gamelog/2022")

count = 0
for datum in data:
    datum.to_csv(f"kd_data{count}.csv")
    count+=1