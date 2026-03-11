#print("Hello World")

import pandas as pd
import numpy as np

shows = pd.DataFrame({
    "show_id": [101, 102, 103,104],
    "title" : ["Star Wars","RuPaul","Knives Out","Alien"],
    "genre": ["Sci-Fi","Reality","Mystery", "Sci-Fi"]

})

#################  Create data in a csv file.. this creates a csv file if it does not exist ############################
shows.to_csv("shows.csv", index =False)
print(shows)

users = pd.DataFrame({
    "user_id": [1,2,3,4,5],
    "name" : ["Alice","Bob","Charlie","Dana", "Eli"],
    "country": ["USA","USA","Canada", "UK","USA"]

})
users.to_csv("users.csv", index =False)
print(users)

watch = pd.DataFrame({
    "user_id":[1,1,2,3,4,5,2,3],
    "show_id": [101,102,101,104,103,101,104,102],
    "watch_minutes":[50,30,45,60,40,25,35,20],
    "date":["2026-01-01","2026-01-02","2026-01-01","2026-01-03","2026-01-01","2026-01-02","2026-01-03","2026-01-01"]
})

watch.to_csv("watch_history.csv", index=False)
print(watch)



####################  To Reda #####################


shows = pd.read_csv("shows.csv")
#watch = pd.read_csv("watch.csv")
#users =pd.read_csv("users.csv")

print("Read shows", shows)
print("Read shows - 5 lines", shows.head(1))
print("Read watch", watch.head(2))
print("Read users", users.head(1))


################################################################

watch.loc[2, "watch_minutes"] = np.nan
watch["watch_minutes"] = watch["watch_minutes"].fillna(0)
print(watch.head())

###########################################

new_watch = pd.DataFrame({
    "user_id":[1,2],
    "show_id": [101,102],
    "watch_minutes":[50,30],
    "date":["2026-01-01","2026-01-02"]

})

print(new_watch)
watch = pd.concat([watch,new_watch])
print(watch)

##############################################

watch_shows = pd.merge(watch,shows,on = "show_id")
print(watch_shows)

genre_watch = watch_shows.groupby("genre")["watch_minutes"].sum()
print(genre_watch)

full_data = pd.merge(watch_shows,users,on = "user_id")
print(full_data)

title = full_data.groupby("title")["watch_minutes"].sum()
print(title)

user_watch = full_data.groupby("name")["watch_minutes"].sum()
print(user_watch)


####################################################
stats = full_data.groupby("genre").agg({
    "watch_minutes":["min", "max", "median"]
})
print(stats)


full_data["title_avg"] = full_data.groupby("name")["watch_minutes"].transform("mean")
print(full_data)

pivot = pd.pivot_table(
    full_data,
    values ="watch_minutes",
    columns ="genre",
    index = "country" ,
    aggfunc ="sum"
  
)

print(pivot)