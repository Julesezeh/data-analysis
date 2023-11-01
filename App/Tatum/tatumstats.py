import pandas as pd

data = pd.read_csv("Tatum2023.csv")

# print(data)
data.rename(
    columns={"Unnamed: 5":"Home/Away","Unnamed: 7":"Win/Loss" },
    inplace=True
    )

print(data.columns.to_list())

fg_shooting_data = (data.loc[:,["Date","PTS","FGA","FG","Opp"]])

three_pts_shooting_data = (data.loc[:,["Date","PTS","3PA","3P","Opp"]])

opps = input("Opp? >").upper()

print(f"Three point shooting data against {opps}")
print(three_pts_shooting_data.loc[three_pts_shooting_data["Opp"] == opps])


print("\n\n\n\n\n")

print(f"Field goals data against {opps}")
opps_fg= fg_shooting_data.loc[fg_shooting_data["Opp"] == opps]
print(opps_fg)


print("\nAverage points scored",opps_fg["PTS"].astype(str).astype(int).mean())


