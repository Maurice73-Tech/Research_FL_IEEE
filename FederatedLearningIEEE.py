import matplotlib.pyplot as plt

df = pd.read_excel("Paper_Daten.xlsx", 'Tabelle2')
print(df)

plt.style.use('seaborn-whitegrid')
plt.plot(df['calender_year'], df['number_of_papers'], marker = 'o')
plt.xlabel('Year', 
           family='Times New Roman', 
           color='b', 
           weight='normal', 
           size = 11,
           labelpad = 6)
plt.ylabel('Number of publications', 
           family='Times New Roman', 
           color='b', 
           weight='normal', 
           size = 11,
           labelpad = 6)
plt.title('Number of publications used by year of publication',
           family='Times New Roman',
           size=14)
plt.grid(True)
labels1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
labels2 = [2017,2018,2019,2020,2021]
plt.yticks(labels1)
plt.xticks(labels2)
plt.show()
