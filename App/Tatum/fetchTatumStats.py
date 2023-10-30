import pandas as pd


logs = {"2023":"https://www.basketball-reference.com/players/t/tatumja01/gamelog/2023","recent":"https://www.basketball-reference.com/players/t/tatumja01/gamelog/2024"}


for urls in logs.items():
    data = pd.read_html(urls[1])
    if urls[0]=='2023':
        data[7].to_csv("Tatum2023.csv")
    elif urls[0]=='recent':
        data[7].to_csv("TatumRecent.csv")

