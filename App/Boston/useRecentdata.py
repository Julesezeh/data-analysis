import pandas as pd

data =  pd.read_csv("Boston_recent_0.csv")

# print(data.columns.to_list())
# print(data)


scores = data.loc[:,["Opponent","Tm","Opp","Date"]]


# opponent = input("Opp?")

# opp_scores = scores.loc[scores['Opponent']==opponent]

# # scores["Tm"] = [int(x) for x in scores["Tm"]]

# #Summation works
# opp_scores["total"] = opp_scores[["Tm","Opp"]].astype(str).astype(int).sum(axis=1)

# print(opp_scores)

active_scores = scores[:3]
active_scores['total'] = active_scores["Tm"].astype(int) + active_scores["Opp"].astype(int)
print(active_scores)
