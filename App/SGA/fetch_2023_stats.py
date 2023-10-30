import pandas as pd


data = pd.read_html("https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2023")

number =  0
for datum in data:
    datum.to_csv(f"shai{number}.csv")
    number +=1