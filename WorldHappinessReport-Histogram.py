# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:07:51 2019

@author: Erkan Çetinyamaç
"""
import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go # import graph objects as "go"

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()

# prepare data
Countries=data.iloc[:,0]
Score=data.iloc[:,1]

trace1 = go.Histogram(
    x=Countries,
    opacity=0.75,
    name = "Countries",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))
trace2 = go.Histogram(
    x=Score,
    opacity=0.75,
    name = "Score",
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

data = [trace1, trace2]
layout = go.Layout(barmode='overlay',
                   title=' Countries vs Scores',
                   xaxis=dict(title='.Countries'),
                   yaxis=dict( title='Score'),
)
fig = go.Figure(data=data, layout=layout)
plot(fig)