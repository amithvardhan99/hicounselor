
""" Recession Analysis using Python """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import *
from sklearn.ensemble import *
from sklearn.neighbors import *
from sklearn.metrics import *
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Task 1
# Now let’s start this task of Recession analysis by importing the necessary Python libraries and the dataset:
def load_the_dataset():
    data = pd.read_csv("UK_monthly_gdp.csv")
    return data

# Task2
def GDP_growth_over_time():
    data = load_the_dataset()
    return data

# TASK 3
# As a recession means the decline in the circulation of money for two consecutive quarters,
# I will convert our monthly data into quarterly data to analyze the recession:
# Convert monthly data to quarterly data using resample method
def monthly_to_quarterly_data():
    data = load_the_dataset()
    df_1 = data.copy()
    df_1["Time Period"] = pd.to_datetime(df_1["Time Period"])
    df_2 = df_1.copy()
    df_2 = df_2.set_index("Time Period")
    df_3 = df_2.resample("3M",closed="left")
    quarterly_data = df_3.mean()
    return quarterly_data


# TASK 4
# Now here’s how we can calculate and analyze recession based on quarterly GDP growth:

# Calculate recession based on quarterly GDP growth
def recession_quarterly_GDP():
    quarterly_data = monthly_to_quarterly_data()
    df_5 = pd.DataFrame(quarterly_data)
    df_5["Recession"] = False
    indices = df_5.index.values
    for i in range(1,len(df_5)):
        if df_5["GDP Growth"][indices[i]]<0 and df_5["GDP Growth"][indices[i-1]]<0:
            df_5["Recession"][indices[i]] = True
    quarterly_data = df_5.copy()
    recess_data = df_5["GDP Growth"][df_5["Recession"]==True]
    fig = px.scatter(x=df_5.index.values,y=df_5["GDP Growth"])
    fig.add_scattergl(x=df_5.index.values,y=df_5["GDP Growth"],line={"color":"green"})
    fig.add_scattergl(x=recess_data.index.values,y=recess_data,line={"color":"red"})
    fig.write_html("fig1.html")
    return quarterly_data
# The red line shows the periods of negative GDP growth (considered recessions),
# and the green line shows the overall trend in GDP growth over time.

# TASK 5
"""Let us now analyze the severity of the recession. The severity of a recession refers to the
extent to which the economy contracts during a recession. A severe recession involves a deeper 
and more prolonged decline in economic activity, resulting in negative effects on employment, 
incomes and other economic indicators. Here’s how to analyze the severity of the recession:"""
def recession_severity():
    quarterly_data = recession_quarterly_GDP()

    return quarterly_data


# load_the_dataset()
# GDP_growth_over_time()
# monthly_to_quarterly_data()
# recession_quarterly_GDP()
# recession_severity()
