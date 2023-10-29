import pandas as pd


boston = pd.read_html("https://www.basketball-reference.com/teams/BOS/2024.html")


# for tables in boston:
#     print(tables)
file_number = 0
for tables in boston:
    tables.to_csv(f"boston{file_number}.csv")