import plotly
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)


data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})

layout = dict(geo = {'scope':'usa'})

choromap = go.Figure(data = [data],layout = layout)

plotly.offline.plot(choromap)

##############################

import plotly.offline as py
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import  plotly
import numpy as np

df = px.data.gapminder().query('year==2007')
fig = px.sunburst(df , path=['continent','country'] , values='pop',
                  color='lifeExp' , hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'],weights=df['pop']))
fig.show()
plotly.offline.plot(fig)