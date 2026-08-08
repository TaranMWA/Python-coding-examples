import numpy as np
import pandas as pd

#website where info is being taken from
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

#only table 3 is needed
tables = pd.read_html(URL)
df = tables[3]

#change to column numbers
df.columns = range(df.shape[1])

#keep columns with index 0 and 2 - name of country and value of GDP
df = df[[0,2]]

#keep the rows 1 to 10 for top 10 economies of the world
df = df.iloc[1:11,:]

#assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']

# print(df) #remove comment to show results

#ammendments to be made to make data more readable

#change data type of the to integer
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

#convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

#round the value to 2 decimal places
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

#rename the column header
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# print(df) #remove comment to show results
df.to_csv('./Largest_economies.csv')
print("Saved sucessfully")

df2 = pd.read_csv('Largest_economies.csv',index_col=0)
print(df2)

