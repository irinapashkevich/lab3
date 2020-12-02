import pandas as pd

df = pd.read_csv(input())
df.drop(['Unnamed: 0'], axis='columns', inplace=True)

df=df.loc[df['STATUS'] == 'OK']

df_U_I=df.loc[df['CONTRACTOR'] == 'Umbrella, Inc']

df=df.sort_values(by='SUM', ascending=False)
print("3 biggest:")
print(df.head(3))

Total = df_U_I['SUM'].sum()
print("")
print("sum of Umbrella, Inc:", Total)