import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(input())
df.drop(['Unnamed: 0'], axis='columns', inplace=True)

names=df["CARGO"].unique()

number=[]
cost=[]
mass=[]

for i in range(len(names)):
    number.append(df.CARGO.value_counts()[names[i]])
    cost.append(df.loc[df['CARGO'] == names[i]]['PRICE'].sum())
    mass.append(df.loc[df['CARGO'] == names[i]]['WEIGHT'].sum())

fig, axs = plt.subplots(nrows=1, ncols=3)
axs[0].bar(names,number)
axs[0].set_title('Number of flights')
axs[1].bar(names,cost)
axs[1].set_title('Total weight')
axs[2].bar(names,mass)
axs[2].set_title('Total price')

plt.show()