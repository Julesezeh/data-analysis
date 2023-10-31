import pandas as pd
import re
teams={"ATL":"HAWKS","BOS":"CELTICS","BKN":"NETS","CHA":"HORNETS","CHI":"BULLS","CLE":"CAVS","DAL":"MAVS","DEN":"NUGGETS","DET":"PISTONS","GSW":"WARRIORS","HOU":"ROCKETS","IND":"PACERS","LAC":"CLIPPERS","LAL":"LAKERS","MEM":"GRIZZLIES","MIA":"HEAT","MIL":"BUCKS","MIN":"TIMBERWOLVES","NOL":"PELICANS","NYK":"KNICKS","OKC":"THUNDER","ORL":"MAGIC","PHI":"76ERS","PHX":"SUNS","POR":"TRAILBLAZERS","SAC":"KINGS","SAS":"SPURS","TOR":"RAPTORS","UTA":"JAZZ","WAS":"WIZARDS"}

print(len(teams))

team = input("What team's data do you need ? (write city code):> ").upper()


if team in teams.keys():
    team_url = input("URL:> ")
    # year = input("year?:> ")
    try:
        data = pd.read_html(team_url)
        year = re.search(r"\d{4}",team_url).group()
        print("worked",year)

        table = ["Regular_season","Playoff" ]
        count=0
        for datum in data:
            datum.to_csv(team+"_"+year+"_"+table[count]+"_stats.csv")
            count+=1

    except:
         print("Error")


# print()