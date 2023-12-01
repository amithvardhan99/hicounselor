import numpy as np
import pandas as pd





#Spearating Train and Test Datasets
def separating_train():
    # do not edit the predefined function name
    df = label_encoding_df()

    # Separate the 'train' DataFrame by excluding rows with value (-1) in 'Stay' column
    train = df[df["Stay"]!=-1]
    # Return the 'train' DataFrame containing only real training data
    return train


def separating_test():
    # do not edit the predefined function name
    df = label_encoding_df()

    # Separate the 'test' DataFrame by selecting rows with value (-1) in 'Stay' column
    test = df[df["Stay"]==-1]

    # Return the 'test' DataFrame containing only the test data with dummy 'Stay' values
    return test





import settings
# Droping duplicate columns
def drop_duplicates_test():
    # do not edit the predefined function name
    test = settings.test

    # Drop specified columns from the 'test' DataFrame ('Stay', 'patientid', 'Hospital_region_code', 'Ward_Facility_Code')
    test1 = test.drop(['Stay', 'patientid', 'Hospital_region_code', 'Ward_Facility_Code'],axis=1,inplace=False)

    # Return the 'test1' DataFrame with duplicate rows removed and specific columns dropped
    return test1



def drop_duplicates_train():
    # do not edit the predefined function name
    train = settings.train
    train1 = train.drop(['case_id', 'patientid', 'Hospital_region_code', 'Ward_Facility_Code'],axis=1,inplace=False)
    # Return the 'train1' DataFrame with duplicate rows removed and specific columns dropped
    return train1


