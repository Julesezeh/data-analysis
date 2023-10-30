import pandas as pd

data = pd.read_csv("boston2.csv",index_col="Player")

shooting_stats = data[["FG","FGA"]]
# print(data.columns.to_list())
print(shooting_stats)