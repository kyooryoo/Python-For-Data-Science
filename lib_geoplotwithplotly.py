# Geographical plotting is challenging for its various kinds of data sources
# plotly can do geo plotting, and matplotlib also have a basemap extension
# for plotting choropleth maps

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations=['AZ','CA','NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['Arizona','California','New York'],
            z=[1.0,2.0,3.0],
            colorbar={'title':'Colorbar Title Goes Here'})
layout = dict(geo={'scope':'usa'})
choromap1 = go.Figure(data=[data],layout=layout)
plot(choromap1)

df = pd.read_csv('2011_US_AGRI_Exports')
print("a data source about US agriculture exports in 2011:\n{}"
      .format(df.head()))
data = dict(type='choropleth',
            colorscale='YIOrRd',
            locations=df['code'],
            locationmode='USA-states',
            z=df['total exports'],
            text=df['text'],
            marker=dict(line=dict(color='rgb(255,255,255)',width=2)),
            colorbar={'title':'Million USD'})
layout = dict(title='2011 US Agriculture Exports by State',
              geo=dict(scope='usa',
                       showlakes=True,
                       lakecolor='rgb(85,173,240)'))
choromap2 = go.Figure(data=[data],layout=layout)
plot(choromap2)

df = pd.read_csv('2014_World_GDP')
print("a data source about the world GDP in 2014:\n{}"
      .format(df.head()))
data = dict(type='choropleth',
            locations=df['CODE'],
            z=df['GDP (BILLIONS)'],
            text=df['COUNTRY'],
            colorbar={'title':'GDP in Billions USD'})
layout = dict(title='2014 Global GDP',
              geo=dict(showframe=False,projection={'type':'Mercator'}))
choromap3 = go.Figure(data=[data],layout=layout)
plot(choromap3)

# reference
# https://plot.ly/python/reference/#choropleth
# https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf
# https://plot.ly/python/offline/
# https://plot.ly/python/colorscales/

# practice
# failed: missing locationmode='country names' settings makes output blank
# locations specify country code in source to API interface
df = pd.read_csv('2014_World_Power_Consumption')
print("a data source about the world power consumption in 2014:\n{}"
      .format(df.head()))
data = dict(type='choropleth',
            locations=df['Country'],
            locationmode='country names',
            z=df['Power Consumption KWH'],
            text=df['Country'],
            colorscale='Viridis',
            reversescale=True,
            colorbar={'title':'KWH'})
layout = dict(title='2014 Power Consumption',
              geo=dict(showframe=False,projection={'type':'Mercator'}))
choromap4 = go.Figure(data = [data],layout = layout)
plot(choromap4)

df = pd.read_csv('2012_Election_Data')
print("a data source about the electioin data in 2012:\n{}"
      .format(df.head()))
data = dict(type='choropleth',
            locations=df['State Abv'],
            locationmode='USA-states',
            z=df['Voting-Age Population (VAP)'],
            text=df['State'],
            colorscale='Viridis',
            reversescale=True,
            colorbar={'title':''})
layout = dict(title='Voting-Age Population',
              geo={'scope':'usa',
                   'showlakes':True,
                   'lakecolor':'rgb(85,173,240)'})
choromap5 = go.Figure(data = [data],layout = layout)
plot(choromap5)