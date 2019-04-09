# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:24:01 2019

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

# import graph objects as "go"
import plotly.graph_objs as go

# Creating trace1
trace1 = go.Scatter(
                    x = Annual_Income,
                    y = Spending_Score,
                    mode = "lines",
                    name = "Annual_Income",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= data.CustomerID)
# Creating trace2
trace2 = go.Scatter(
                    x = Age,
                    y = Spending_Score,
                    mode = "lines+markers",
                    name = "Age",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= data.CustomerID)
data = [trace1, trace2]
layout = dict(title = 'Spending Score vs Age and Income',
              xaxis= dict(title= 'Annual_Income --- Age',ticklen= 5,zeroline= False)
             )
fig = dict(data = data, layout = layout)
plot(fig)