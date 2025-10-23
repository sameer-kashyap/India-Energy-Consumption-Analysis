import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('master_dataset.xlsx')

df_sorted = df.sort_values(by='Total_Generation', ascending=False)


top_10 = df_sorted.head(10)

top_10 = top_10.iloc[::-1]


states = top_10['State']
generation = top_10['Total_Generation']

plt.figure(figsize=(10, 6))


plt.barh(states, generation)


plt.title('Top 10 States by Total Energy Generation')
plt.xlabel('Total Generation (MW)')
plt.ylabel('State')


plt.show()