import pandas as pd

data =  pd.read_csv("Boston_regular_season_2023.csv")

# print(data.columns.to_list())
# print(data)


scores = data.loc[:,["Opponent","Date","Tm","Opp"]]

print(scores.loc[scores['Opponent']=="Washington Wizards"])
# print(scores)
# print(scores.loc[:,"Tm"])