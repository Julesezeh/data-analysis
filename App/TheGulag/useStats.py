import pandas as pd

file = input("file: ")
data =  pd.read_csv(file)

# print(data.columns.to_list())
# print(data)

data.rename(
    columns={"Unnamed: 5":"Home/Away" },
    inplace=True
    )
scores = data.loc[:,["Opponent","Tm","Opp","Date","Home/Away"]]

print(scores)

opponent = input("Opp?")

opp_scores = scores.loc[scores['Opponent']==opponent]

# scores["Tm"] = [int(x) for x in scores["Tm"]]

#Summation works
opp_scores["total"] = opp_scores[["Tm","Opp"]].astype(str).astype(int).sum(axis=1)

print(opp_scores)


