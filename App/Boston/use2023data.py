import pandas as pd

data =  pd.read_csv("Boston_regular_season_2023.csv")

# print(data.columns.to_list())
# print(data)


scores = data.loc[:,["Opponent","Tm","Opp"]]


opponent = input("Opp?")

opp_scores = scores.loc[scores['Opponent']==opponent]

opp_scores["total"] = int(scores["Tm"]) + int(scores["Opp"])

print(opp_scores)
# print(scores)
# print(scores.loc[:,"Tm"])