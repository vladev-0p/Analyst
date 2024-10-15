import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob

df = pd.read_csv('netflix_titles.csv')

print(df.shape)

data_set = df.iloc[:4, 1:4]
print(data_set[~data_set['director'].isna()])  #filter None data for column director
print(df.columns)


summ = df.groupby(['rating']).size().reset_index(name='counts') #size - аналог count(*) SQL
print(summ)
# '''Diagram '''
# pieChart = px.pie(summ, values='counts' , names='rating', title='Distribution of content ratings on Netflix')
#
# pieChart.show()
#
'''Filtering top 5 directors'''
#
# df['director']=df['director'].fillna('Director not specified')

# directors_list = pd.DataFrame()
# directors_list = df['director'].str.split(',', expand=True).stack()
#
# directors_list = directors_list.to_frame(name='director')
# print(directors_list)
#
# unique_director = directors_list.groupby(['director']).size().reset_index(name='total').sort_values(by='total',
#                                                                                                     ascending=False).head()
#
# print(unique_director)
#
# top5direc = px.bar(unique_director, x='director', y='total')
#
# top5direc.show()

# '''Sorting top 5 actors'''
# unsorted_actors=pd.DataFrame()
#
#
#
# unsorted_actors =df['cast'].str.split(',',expand=True).stack().to_frame(name='Actor')
#
# grouped_actors=unsorted_actors.groupby('Actor').size().reset_index(name='Total Films').sort_values(by='Total Films' ,ascending=False)
#
# top5actors= grouped_actors.head()
#
# actorsdiagramm= px.bar(top5actors, x='Actor', y='Total Films')
# actorsdiagramm.show()

'''Analysing released year and type of films'''

data_df = df[['type', 'release_year']]

print(data_df)

data_type = df.groupby('type').size().reset_index(name='Total Types ')

data_year = df.groupby('release_year').size().reset_index(name='Total Films in Year')

print(data_type)

print(data_year)

data_year_type = df.groupby(['release_year', 'type']).size().reset_index(name='Total Count')

print(data_year_type)

graph = px.line(data_year, 'release_year', 'Total Films in Year')

graph.show()

data_country = df.groupby('country').size().reset_index(name='Total films  in each country').sort_values(
    by='Total films  in each country', ascending=False)

print(data_country)

'''Sentiment Analysis'''

df2 = df[['release_year', 'description']]

df2 = df.rename(columns={'release_year': 'Release Year', 'description': 'Description'})

for index, row in df2.iterrows():
    d = row['Description']
    testimonial = TextBlob(d)
    p = testimonial.sentiment.polarity
    if p == 0:
        sent = 'Neutral'
    elif p > 0:
        sent = 'Positive'
    else:
        sent = 'Negative'

    df2.loc[[index, 2], 'Sentiment'] = sent

df2 = df2.groupby(['Release Year', 'Sentiment']).size().reset_index(name='Total Count')

df2 = df2[df2['Release Year'] > 2005]

barGraph = px.bar(df2, x='Release Year', y='Total Count', color='Sentiment', title='total Analysis of Content')

barGraph.show()
