# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:56:51 2019

@author: Erkan Çetinyamaç
"""

import pandas as pd
import numpy as np

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\Mall_Customers.csv", encoding="cp1252")

data.info()
data.head()
# import figure factory
import plotly.figure_factory as ff
# prepare data

dat = data.loc[:,["Gender","Age", "Spending Score (1-100)"]]
dat["index"] = np.arange(1,len(dat)+1)
# scatter matrix
fig = ff.create_scatterplotmatrix(dat, diag='box', index='index',colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
plot(fig)