import pandas as pd


data = pd.read_html("https://www.basketball-reference.com/players/g/gilgesh01/gamelog/2024")

data[7].to_csv(f"shaiRecent.csv")
