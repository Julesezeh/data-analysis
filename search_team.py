def search(shooting_stats):
    opps = input("Opposition team? ")
    print(shooting_stats.loc[shooting_stats["Opp"] == opps])

