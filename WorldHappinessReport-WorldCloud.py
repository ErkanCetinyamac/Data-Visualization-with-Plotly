# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:14:18 2019

@author: Erkan Çetinyamaç
"""
import pandas as pd

# Plotly library usage in Spyder
from plotly.offline import plot
import plotly.graph_objs as go # import graph objects as "go"

from wordcloud import WordCloud # Word Cloud library usage in Spyder

data=pd.read_csv(r"C:\Users\eceti\Desktop\phyton\DataAi\Data Visualization\WorldHappinessReport.csv", encoding="cp1252")

data.info()
data.head()

# data prepararion
Countries=data.iloc[:,0]
plt.subplots(figsize=(8,8))
wordcloud = WordCloud(
                          background_color='white',
                          width=512,
                          height=384
                         ).generate(" ".join(x2011))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png')

plt.show()