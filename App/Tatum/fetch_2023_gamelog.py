import pandas as pd

data = pd.read_html("https://www.basketball-reference.com/players/t/tatumja01/gamelog/2023")

file_number = 0
for datum in data:
    datum.to_csv(f"tatum{file_number}.csv")
    file_number+=1