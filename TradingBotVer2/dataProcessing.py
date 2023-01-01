import pandas as pd 

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
data = pd.read_html(url)
df = data[1]
data[1].head() 

df = df.sort_index(ascending = False )
newDf = df[[("Date", "Date"), ("Added", "Ticker"), ("Removed", "Ticker")]]
newDf.columns = newDf.columns.get_level_values(0)
newDf.head()
print(list(set(newDf["Added"].dropna()).union(set(newDf["Removed"].dropna()))))
rows = {}
for i in range(len(newDf)):
    date = newDf["Date"][i]
    if date in rows:
        continue
    temp = newDf[newDf["Date"] == date ]
    temp.reset_index(inplace = True)
    addedList = []
    removedList = []
    for j in range(len(temp)):
        if type(temp["Added"][j]) == str:
            addedList.append(temp["Added"][j])
        if type(temp["Removed"][j]) == str:
            removedList.append(temp["Removed"][j])
    rows[date] = {"added": addedList, "removed": removedList}

final_df = pd.DataFrame(rows).T
final_df.index = pd.to_datetime(final_df.index)
final_df = final_df.sort_index(ascending=True)
final_df.reset_index(inplace=True)
final_df.head()

def transform(x):
    st = ""
    for i in x:
        st += i + ""
    return st

final_df["added"] = final_df["added"].apply(transform)
final_df["removed"] = final_df["removed"].apply(transform)

final_df.to_csv("SPYChanges.csv", index=False)