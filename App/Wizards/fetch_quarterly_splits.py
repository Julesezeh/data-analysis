import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/teams/WAS/2024/splits/"
        )

count=0
for datum in data:
    datum.to_csv("Wizards_splits_{count}.csv")
    count+=1