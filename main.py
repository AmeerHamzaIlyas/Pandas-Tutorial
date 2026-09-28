import pandas as pd
df = pd.read_csv("people-data-pandas-analysis.csv")
print(df)
data = {
    "name":["Ameer","Nasir","Yasir"],
     "age":[21,27,29],
    " country":["Pakistan","Pakistan","Brazil"],
    "cost":[300,600,900]
}
df = pd.DataFrame(data)
print(f"This is manual created data-frame {df}")
