import pandas as pd
covid = pd.read_csv("COVID.csv")

# Choose entries with county Name of Cork.
Corkonly  = covid[covid['CountyName'] == 'Cork']
Dublin  = covid[covid['CountyName'] == 'Dublin']


print(Corkonly.to_string())
