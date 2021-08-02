import pandas
import plotly.figure_factory as ff
import csv

df = pandas.read_csv('/Users/Aadi/Downloads/project108/data.csv')

fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg Rating'])
fig.show()