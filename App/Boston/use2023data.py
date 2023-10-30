import pandas as pd

data =  pd.read_csv("Boston_regular_season_2023.csv")

# print(data.columns.to_list())
# print(data)


scores = data.loc[:]


opponent = input("Opp?")
print(scores.loc[scores['Opponent']==opponent])
# print(scores)
# print(scores.loc[:,"Tm"])