import sys
import io
import numpy as np
import traceback
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
def read_data_from_csv():
    df = pd.read_csv("playstore_apps.csv")
    return df


#Task2: Keep Only Required columns,
def remove_unwanted_columns():
    #do not remove this line and do not change the function names
    df=read_data_from_csv()
    df.drop(["Last Updated","Current Ver","Android Ver","Size"],axis=1,inplace=True)
    #remove the unwanted column and use inplace= True for dynamically updating the dataset
    # write your code here
    return df


#TASK3 : REMOVE DUPLICATES FROM THE DATASET
def remove_duplicates():
    # do not remove this line and do not change the function names
    df=remove_unwanted_columns()
    df.drop_duplicates(inplace=True)
    return df


#TASK4: HANDLE NULL VALUES IN THE DATASET
def no_of_null_values():
    df= remove_duplicates()
    ##write your code here and return the null values
    df_2 = df.isna().sum()
    return df_2


#TASK5: Replace the null values

def prob(df_3):
    gg = df_3.value_counts()
    il = list(gg.index)
    ig = list(gg.values)
    kk = ig.index(max(ig))
    mm = il[kk]
    return mm


def replace_null_values():
    df=remove_duplicates()
    df_2 = df.copy()
    df_3 = df_2.copy()
    df_3["Rating"] = df_3["Rating"].fillna(df_2["Rating"].mean())
    df_3["Reviews"] = df_3["Reviews"].fillna(df_2["Reviews"].mean())
    df_3["Installs"] = df_3["Installs"].fillna(df_2["Installs"].mean())
    df_3["Price"] = df_3["Price"].fillna(df_2["Price"].mean())
    df_3["Type"] = df_3["Type"].fillna(prob(df_3["Type"]))
    df_3["Content Rating"] = df_3["Content Rating"].fillna(prob(df_3["Content Rating"]))
    # write your code here
    return df_3


#TASK6: check unique values of Category column and remove irrelevant category
def check_unique_values():
    df= replace_null_values()
    df = df[df["Category"]!="1.9"]
    #write your code here
    return df



#TASK7: Check unique values of "Type" column,
def free_or_paid():
    df= check_unique_values()
    #write your code here
    return df["Type"].value_counts()




# Task 8: Remove apps with irrelevant names. starting with '?'
##export the cleaned dataset to new file as 'cleaned_apps_db.csv'
def irrleveant_names():
    df=check_unique_values()
    df = df[df["App"].str.startswith("?")==False]

    df.to_csv('cleaned_apps_db.csv', index=False)
    return df


#Task9: Remove rows with nan values in the  Reviews dataset
#Read the playstore_reviews.csv file as df1 and return the same

def reviews_dataset():
    #write your code here
    df = pd.read_csv("playstore_reviews.csv")
    df1 = df.dropna(inplace=False)
    return df1


#Task10: Remove identical rows from the dataset and upload the dataset to the database
#export the cleaned dataset to new file as 'cleaned_reviews_db.csv'
def remove_identical_rows():
    df1 = reviews_dataset()
    df1.drop_duplicates(inplace=True)
    df1.to_csv('cleaned_reviews_db.csv', index=False)
    return df1


#TASK 11
#follow the instruction in the Task 11 description and complete the task as per it.

#check if mysql table is created using "cleaned_apps_db.csv" and "cleaned_reviews_db.csv"
#Use this final dataset and upload it on the provided database for performing analysis in  MySQL
#To run this task click on the terminal and click on the run project






