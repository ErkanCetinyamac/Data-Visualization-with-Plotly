# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:43:17 2019

@author: Erkan Çetinyamaç
"""
import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()

# data preparation
HappinessRank=data.iloc[:,2]
Countries=data.iloc[:,0]

trace0 = go.Box(
    y=HappinessRank,
    name = 'HappinessRank',
    marker = dict(
        color = 'rgb(12, 12, 140)',
    )
)
trace1 = go.Box(
    y=Countries,
    name = 'Countries',
    marker = dict(
        color = 'rgb(12, 128, 128)',
    )
)
data = [trace0, trace1]
plot(data)