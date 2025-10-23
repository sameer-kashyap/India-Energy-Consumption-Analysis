import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('master_dataset.xlsx')


df_filtered = df[df['Per_Capita_Income'] > 0]


income = df_filtered['Per_Capita_Income']
energy = df_filtered['Total_Generation']


plt.figure(figsize=(8, 5))


plt.scatter(x=income, y=energy)


plt.title('Relationship: Per Capita Income vs. Energy Generation')
plt.xlabel('Per Capita Income (INR)')
plt.ylabel('Total Generation (MW)')


plt.grid(True)


plt.show()