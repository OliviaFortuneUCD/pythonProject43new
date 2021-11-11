import pandas as pd
covid = pd.read_csv("COVID.csv")

# Choose entries with county Name of Cork.
Corkonly  = covid[covid['CountyName'] == 'Cork']



print(Corkonly.to_string())
