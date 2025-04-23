# script to update seminars TSV
import pandas as pd
from datetime import datetime

def is_future_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    current_date = datetime.now()
    return date_obj > current_date

past = pd.read_csv("../Seminars/past_seminars.tsv", sep="\t")
upcoming = pd.read_csv("../Seminars/upcoming_seminars.tsv", sep="\t")

# TODO check if empty or TBA

for i in range(len(upcoming)):

    date = upcoming.iloc[i]["Date"].replace('"', "")
    if is_future_date(date):
        continue
    else:
        print("past seminar")
        past = pd.concat([past, upcoming.iloc[[i]]], ignore_index=True)
        upcoming_new = upcoming.drop(i, inplace=False)

past.to_csv("../Seminars/past_seminars.tsv", sep="\t", index=False)
try:
    upcoming_new
except NameError:
    print("No updates")
else:
    upcoming_new.to_csv("../Seminars/upcoming_seminars.tsv", sep="\t", index=False)    
    print("Updated past and upcoming seminars TSV files.")

