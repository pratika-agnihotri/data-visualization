import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1          = pd.read_csv('dataset.csv', 
                  usecols=['dateRep', 'cases', 'deaths', 'countriesAndTerritories'])

data1.countriesAndTerritories[data1['countriesAndTerritories']=='United_States_of_America']='USA'

data2          = data1.groupby('countriesAndTerritories', as_index=False).sum()
data3          = data2.sort_values('cases').tail(20)[::-1]

yaxis          = data3['countriesAndTerritories']
xaxis          = data3['cases']
x1axis         = data3['deaths']
# print(xaxis, yaxis)

fig            = plt.figure(figsize=(14,10))
ax             = fig.gca()
plt.barh(yaxis, xaxis, color='#EA3F5A' )
plt.barh(yaxis, x1axis,left=xaxis,  color='#00A1AB')

plt.xlabel("Cases And Deaths")
plt.ylabel("Countries")
plt.title("Total Cases and Deaths in Top 20 Most Corona Affected Countries", fontsize=17,
fontweight='heavy', fontname='Georgia', color='#00a1ab')
plt.xticks(rotation=45)

major_ticks    = np.arange(0,1500000,90000)
minor_ticks    = np.arange(0,1500000,30000)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
plt.xticks(fontname='Arial')
plt.yticks(fontname='Arial')
plt.legend(["Cases", "Deaths"])

ax.grid(b=True, which='major', color='#a4c5c6',linestyle='-')
ax.grid(b=True, which='minor', color='#ffb6b6',linestyle='--')

from matplotlib.offsetbox import AnchoredText
at = AnchoredText("Data Source:European Centre for Disease Prevention and Control",
                  prop=dict(size=8), frameon=True,
                  loc='upper center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

ax.text(950000, 23, "This Graph is based on data collected till 05/05/2020 ", fontsize=8)

plt.show()

