import pandas as pd

def fetch_stats(url):
    data = pd.read_html(url)
    return data