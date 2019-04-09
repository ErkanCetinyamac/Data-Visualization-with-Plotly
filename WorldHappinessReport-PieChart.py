# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:23:27 2019

@author: Erkan Çetinyamaç
"""

# data preparation

import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go # import graph objects as "go"

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()

# prepare data frame

HappinessRank=data.iloc[:5,2]
Countries=data.iloc[:5,0]


# figure
fig = {
  "data": [
    {
      "values": HappinessRank,
      "labels": Countries,
      "domain": {"x": [0, .5]},
      "name": "Happiness pie chart",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Countries Happiness Rank",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Happiness Rank",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
plot(fig)