import pandas as pd

season = input("Old(O) or Recent(R)").upper()
proceed = None

if season == "O":
    data = pd.read_csv("Stewart2023.csv")
    proceed = True
elif season == "R":
    data = pd.read_csv("StewartRecent.csv")

else:
    "Invalid"

rebound_data =  data.loc[:,["Opp","TRB","Date"]]

if season=="O":
    ask =  input("What team? ").upper()
    print(rebound_data.loc[rebound_data["Opp"]==ask])
else:
    print(rebound_data)