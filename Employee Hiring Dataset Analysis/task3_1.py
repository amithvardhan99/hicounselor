import numpy as np
import matplotlib.pyplot as plt
from settings import connect_database, load_records

#plot_non_filled_and_offerd_jobs predefined function returns the nonfilled jobs and offered jobs wrt month and save the graph to visualize
#all the graph can be viewed in the plotting folder, we need to save the graph with respective tasks along with the naming convention

def plot_non_filled_and_offerd_jobs():
    #write your code here
    arrNonfilledjobs = None
    arrOfferedJobs = None
    return arrNonfilledjobs, arrOfferedJobs



def task_runner():
    arrNonfilledjobs, arrOfferedJobs = plot_non_filled_and_offerd_jobs()
    print(arrNonfilledjobs)
    print(arrOfferedJobs)

# plot_non_filled_and_offerd_jobs()
