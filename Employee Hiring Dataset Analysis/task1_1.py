import numpy as np
import matplotlib.pyplot as plt
from settings import connect_database, load_records

#plot_arrfilled_arrnonfilled predefined function returns the values of filled jobs and non filled jobs of all the months and plot the graph
def plot_arrfilled_arrnonfilled():
    #write your code here
    arrFilledjobs = None
    arrNonfilledjobs = None
    return arrFilledjobs, arrNonfilledjobs



def task_runner():
    arrFilledjobs, arrNonfilledjobs = plot_arrfilled_arrnonfilled()
    print(arrFilledjobs)
    print(arrNonfilledjobs)
