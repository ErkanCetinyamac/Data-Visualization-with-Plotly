# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:17:03 2019

@author: Erkan Çetinyamaç

Mall Customer Segmentation Data
Market Basket Analysis with Plotly
"""

import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\Mall_Customers.csv", encoding="cp1252")

data.info()
data.head()

#Slicing Columns
Annual_Income=data.iloc[:,3]
Spending_Score=data.iloc[:,4]
Gender=data.iloc[:,1]
# create trace1 
trace1 = go.Bar(
                x = Gender,
                y = Annual_Income,
                name = "Income ",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = data.CustomerID)
# create trace2 
trace2 = go.Bar(
                x = Gender,
                y = Spending_Score,
                name = "Spending Score (1-100)",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = data.CustomerID)
data = [trace1, trace2]
layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
plot(fig) # Gender vs Income and spending score
