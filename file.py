import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
stdev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_stdev_start, first_stdev_end = mean-stdev, mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev), mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev), mean+(3*stdev)

fig = ff.create_distplot([data], ["Reading Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="Standard Deviation 2"))
fig.show()

thin_1_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
thin_2_stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
thin_3_stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]
print("The mean is {}".format(mean))
print("The median is {}".format(median))
print("The mode is {}".format(mode))
print("The standard deviation of this data is {}".format(stdev))
print("{}% of the data lies within 1 standard deviation".format(len(thin_1_stdev)*100.0/len(data)))
print("{}% of the data lies within 2 standard deviations".format(len(thin_2_stdev)*100.0/len(data)))
print("{}% of the data lies within 3 standard deviations".format(len(thin_3_stdev)*100.0/len(data)))