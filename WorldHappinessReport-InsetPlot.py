# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:09:22 2019

@author: Erkan Çetinyamaç
"""
import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go # import graph objects as "go"

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()


# data preparation
HappinessRank=data.iloc[:,2]
Countries=data.iloc[:,0]
Family=data.iloc[:,6]
WhiskerHigh=data.iloc[:,3]
Freedom=data.iloc[:,8]
# import figure factory
import plotly.figure_factory as ff
# first line plot
trace1 = go.Scatter(
    x=HappinessRank,
    y=WhiskerHigh,
    name = "WhiskerHigh",
    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
)
# second line plot
trace2 = go.Scatter(
    x=HappinessRank,
    y=Freedom,
    xaxis='x2',
    yaxis='y2',
    name = "Freedom",
    marker = dict(color = 'rgba(160, 112, 20, 0.8)'),
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2',        
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2',
    ),
    title = 'Happiness'

)

fig = go.Figure(data=data, layout=layout)
plot(fig)