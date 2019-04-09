# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:52:20 2019

@author: Erkan Çetinyamaç


"""


import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\Mall_Customers.csv", encoding="cp1252")

data.info()
data.head()

# prepare data frame

Annual_Income=data.iloc[:,3]
Spending_Score=data.iloc[:,4]
Age=data.iloc[:,2]


# create trace 1 that is 3d scatter
trace1 = go.Scatter3d(
    x=Spending_Score,
    y=Age,
    z=Annual_Income,
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255,0,0)',                # set color to an array/list of desired values      
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0  
    )
    
)
fig = go.Figure(data=data, layout=layout)
plot(fig)