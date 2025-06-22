import pandas as pd

df = pd.read_csv('"Z:\\mora\\פייתון\\פייתון מתקדם\\5\\cities.csv"')
df.isnull().sum()
df.City = df.City.fillna(0)
df = df.drop_duplicates()
average_population = df.groupby['LatD'].mean()

largest_city = df.loc[df['LatD'].idxmax()]

smallest_city = df.loc[df['LatD'].idxmin()]

df = df.rename(columns={"אוכלוסיה": "Population"})

df['Population per km²'] = df['Population'] / df['Area']

