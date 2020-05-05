import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# my_numpy_array = np.random.rand(3)
# array_2d = np.random.rand(3,2)

# my_first_series = pd.Series(my_numpy_array)

# my_first_df = pd.DataFrame(array_2d)

# print(type(my_numpy_array))
# # print(my_first_series)
# print()
# series = pd.Series(my_numpy_array, index=["First", "Second", "Third"])
# print(series)
# print(series.index)
# print(my_first_df)

# print(my_first_df)
# print(my_first_df.columns)
# my_first_df.columns= ["First", "Second"]
# print(my_first_df)


# df= pd.read_csv('dataset.csv', nrows=7)
# print(df.columns)

df= pd.read_csv('dataset.csv', 
usecols=['dateRep', 'countriesAndTerritories', 'cases', 'deaths'])
# print(df)

# df.to_pickle(os.path.join('..', 'data_frame.pickle'))    #dont know this exactly

# countries = df['countriesAndTerritories']
# all_countries = pd.unique(countries)
# print(len(all_countries))

# s = df['countriesAndTerritories']=='India'
# print(s.value_counts())
# print()
# print(s)

# india_df = df.loc[ df['countriesAndTerritories']=='India', :]
# america_df = df.loc[df['countriesAndTerritories']=='United_States_of_America', :]
# print(mydf.to_string())

# sampledf = df.loc[1035, 'countriesAndTerritories']
sampledf = df.loc[2600, ]
# print(sampledf)

sampledf = df.iloc[0, 0]
# print(sampledf)

sampledf = df.iloc[0, :]
# print(sampledf)

sampledf = df.iloc[0:2, 0:2]
# print(sampledf)

# print(type(df['dateRep']))
least_death = df['deaths'].sort_values().head()
max_deaths = df['deaths'].sort_values().tail()

# print(df.iloc[12538, :])
# print()
# print(df.iloc[6502, :])

''' SUM OF DEATHS IN AMERICA AND INDIA '''
# print(india_df['deaths'].sum())
# print(america_df['deaths'].sum())


''' GROUP BY '''
# print(india_df)      # from 5534 till 5649
# print(type(india_df))
# for name, group in india_df.groupby('countriesAndTerritories'):
#    print(name)
#    print(group)
#    break

# aggregate = df.groupby('countriesAndTerritories').agg(np.min)

# print(america_df[america_df['deaths']==america_df['deaths'].max()])
# print(india_df[india_df['deaths']==india_df['deaths'].max()])

# print(df['deaths'].max())

''' Writing data to Excel '''
# america_df.to_excel("coviddata.xlsx")
# america_df.to_excel("coviddata.xlsx", index=False)

''' calculating number of deaths in America and India and Italy in last 15 days '''
india_df    = df.loc[df['countriesAndTerritories']=='India', :]
a_df  = df.loc[df['countriesAndTerritories']=='United_States_of_America' , :]
i_df    = df.loc[df['countriesAndTerritories']=='Italy', :]

india_data, a_data, i_data  = india_df.head(15), a_df.head(15), i_df.head(15)
# print("--------------------- INDIA DATA ------------------")
# print(india_data)
# print('\n\n AFTER ILOC \n\n')
# print(india_data.iloc[::-1])
# print(type(india_data))
# print(india_data.dtypes)
# print("--------------------- AMERICA DATA ------------------")
# print(a_data)
# print("--------------------- ITALY DATA ------------------")
# print(i_data)

''' Graph plotting '''
fig = plt.figure()
ax = fig.gca()

xaxis    = np.array(india_data.iloc[::-1]['dateRep'])

yaxis    = np.array(india_data.iloc[::-1]['deaths'])

plt.plot(xaxis, yaxis, 'om-' )

# am_yaxis = np.array(a_data.iloc[::-1]['deaths'])
# plt.plot(xaxis, am_yaxis, 'ob-')

# it_yaxis = np.array(i_data.iloc[::-1]['deaths'])
# plt.plot(xaxis, it_yaxis, 'og-')

plt.xticks(rotation=24)
plt.grid(True, linestyle='--', color='lightgrey')

plt.xlabel('Date', fontsize='14', color='maroon')
plt.ylabel('Number of Deaths', fontsize='14', color='maroon')
plt.title("Deaths In India In Last 15 days Due To Coronavirus", fontsize='17', color='maroon')
plt.xticks(fontname='Arial')

'''SOURCE'''
from matplotlib.offsetbox import AnchoredText
at = AnchoredText("Data Source:European Centre for Disease Prevention and Control",
                  prop=dict(size=8), frameon=True,
                  loc='lower right',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

''''''
plt.show()



# DEATH = india_data['deaths']
# print(type(DEATH))

# print(type(np.array(india_data['deaths'])))


