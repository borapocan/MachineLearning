import matplotlib as mpl
import matplotlib.pyplot as plt
import folium
import numpy as np
import pandas as pd

# Question 1
df_sr = pd.read_csv('https://cocl.us/datascience_survey_data',index_col=0)

# Question 2
# Sorting the values based on Very interested
df_sr.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)
# Taking the percentage of the responses and rounding it to 2 decimal places
df_sr = round((df_sr/2233)*100,2)
# View top 5 rows of the data
df_sr.head()
# Plotting
ax = df_sr.plot(kind='bar',
                figsize=(20, 8),
                rot=90,color = ['#5cb85c','#5bc0de','#d9534f'],
                width=.8,fontsize=14)
# Setting plot title
ax.set_title('Percentage of Respondents Interest in Data Science Areas',fontsize=16)
# Setting figure background color
ax.set_facecolor('white')
# setting legend font size
ax.legend(fontsize=14,facecolor = 'white')
# Removing the Border
ax.get_yaxis().set_visible(False)
# Creating a function to display the percentage.
for p in ax.patches:
    ax.annotate(np.round(p.get_height(),decimals=2),
                (p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 10),
                textcoords='offset points',
                fontsize = 14)
#plt.show()


# Question 3
df_sfc = pd.read_csv('https://cocl.us/sanfran_crime_dataset')

# Assigning a variable with the total counts of each Neighborhood
df_neig= df_sfc['PdDistrict'].value_counts()

# Assigning the values of the variable to a Pandas Data frame
df_neig1 = pd.DataFrame(data=df_neig.values, index = df_neig.index, columns=['Count'])

# Reindexing the data frame to the requirement
df_neig1 = df_neig1.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])

# Resetting the index
df_neig1 = df_neig1.reset_index()

# Assigning the column names
df_neig1.rename({'index': 'Neighborhood'}, axis='columns', inplace=True)

# Question 4
# I did all the imports at the top
# read the file
geojson = r'world_countries.json'
# map centering
sf_map = folium.Map(location = [37.77, -122.42], zoom_start = 12)
# to display
sf_map.choropleth(geo_data=geojson,
                  data=df_neig1,
                  columns=['Neighborhood', 'Count'],
                  key_on='feature.properties.DISTRICT',
                  fill_color='YlOrRd',
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name='Crime Rate in San Francisco')











