import pandas as pd

data =  pd.read_csv("Boston_regular_season_2023.csv")

# print(data.columns.to_list())
# print(data)


scores = data.loc[:,["Opponent","Tm","Opp","Date"]]


opponent = input("Opp?")

opp_scores = scores.loc[scores['Opponent']==opponent]

# scores["Tm"] = [int(x) for x in scores["Tm"]]

#Summation works
opp_scores["total"] = opp_scores[["Tm","Opp"]].astype(str).astype(int).sum(axis=1)

print(opp_scores)


