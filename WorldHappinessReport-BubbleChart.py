# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:59:28 2019

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


data1 = [
    {
        'y': Freedom,
        'x': WhiskerHigh,
        'mode': 'markers',
        'marker': {
            'color': HappinessRank,
            'size': HappinessRank,
            'showscale': True
        },
        "text" :  Countries   
    }
]
plot(data1)