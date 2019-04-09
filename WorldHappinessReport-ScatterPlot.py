# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:56:48 2019

@author: Erkan Çetinyamaç
"""

import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go # import graph objects as "go"

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()

# prepare data frame

HappinessRank=data.iloc[:,2]
Family=data.iloc[:,6]
HealthLifeExpectance=data.iloc[:,7]
Freedom=data.iloc[:,8]





# creating trace1
trace1 =go.Scatter(
                    x = HappinessRank,
                    y = data.Family,
                    mode = "markers",
                    name = "Family",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= data.Country)
# creating trace2
trace2 =go.Scatter(
                    x = HappinessRank,
                    y = HealthLifeExpectance,
                    mode = "markers",
                    name = "HealthLifeExpectance",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= data.Country)
# creating trace3
trace3 =go.Scatter(
                    x = HappinessRank,
                    y = Freedom,
                    mode = "markers",
                    name = "Freedom",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= data.Country)
data = [trace1, trace2, trace3]
layout = dict(title = 'Happiness Rank vs HealthLifeExpectance, Freedom and Family ',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Family - Health - Freedom',ticklen= 5,zeroline= False)
             )
fig = dict(data = data, layout = layout)
plot(fig)
