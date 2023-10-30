import pandas as pd

season = input("Old(O) or Recent(R)").upper()
proceed = None

if season == "O":
    data = pd.read_csv("Giannis2023.csv")
    proceed = True
elif season == "R":
    data = pd.read_csv("GiannisRecent.csv")
    three_point_shooting_stats = data.loc[:,["Date","3P","3PA","Opp","PTS"]]
    field_goals_stats = data.loc[:,["Date","FG","FGA","Opp","PTS"]]
    print(three_point_shooting_stats)
    print("\n\n\n")
    print(field_goals_stats)


else:
    "Invalid"



if proceed:
    three_point_shooting_stats = data.loc[:,["3P","3PA","Opp","PTS"]]
    field_goals_stats = data.loc[:,["FG","FGA","Opp","PTS"]]

    stats = input("3P stats(3) or FG stats(G)").upper()
    if stats == "3":
        team = input("What team? ").upper()
        print("Three point stats against ",team)
        print(three_point_shooting_stats.loc[three_point_shooting_stats["Opp"]==team])
    elif stats == "G":
        team = input("What team? ").upper()
        print("Field goal stats against ",team)
        print(field_goals_stats.loc[field_goals_stats["Opp"]==team])
    else:
        team = input("What team? ").upper()
        print("Three point stats against ",team)
        print(three_point_shooting_stats.loc[three_point_shooting_stats["Opp"]==team])
        print("\n\n\n\n")
        print("Field goal stats against ",team)
        print(field_goals_stats.loc[field_goals_stats["Opp"]==team])


# print(data.columns.to_list())