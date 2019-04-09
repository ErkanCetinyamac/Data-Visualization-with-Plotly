# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:54:45 2019

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
Gender=data.iloc[:,1]
Index=data.iloc[:,0]

trace1 = go.Scatter(
    x=Spending_Score,
    y=Gender,
    name = "research"
)
trace2 = go.Scatter(
    x=Spending_Score,
    y=Age,
    xaxis='x2',
    yaxis='y2',
    name = "citations"
)
trace3 = go.Scatter(
    x=Spending_Score,
    y=Annual_Income,
    xaxis='x3',
    yaxis='y3',
    name = "income"
)
trace4 = go.Scatter(
    x=Spending_Score,
    y=Index,
    xaxis='x4',
    yaxis='y4',
    name = "total_score"
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis3=dict(
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    ),
    title = 'Spending_Score'
)
fig = go.Figure(data=data, layout=layout)
plot(fig)
