import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates

df = pd.read_excel("Paper_Daten.xlsx", 'Tabelle2')
print(df)

plt.plot(df['calender_year'], df['number_of_papers'])
plt.xlabel('Year', 
           family='serif', 
           color='b', 
           weight='normal', 
           size = 11,
           labelpad = 6)
plt.ylabel('Number of papers', 
           family='serif', 
           color='b', 
           weight='normal', 
           size = 11,
           labelpad = 6)
plt.title('Number of papers used by year of publication')
plt.grid(True)
labels = [2017,2018,2019,2020,2021]
plt.xticks(labels)
plt.show()
