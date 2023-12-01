import numpy as np
import pandas as pd


np.set_printoptions(suppress=True)
import warnings
warnings.filterwarnings('ignore')

# Importing datasets

def read_train_data():
    train = pd.read_csv("train.csv")
    return train


def read_test_data():
    # read the test.csv file using pandas library and return it
    test = pd.read_csv("test.csv")
    return test





# NA values in train dataset
def check_null_values_train():
    # do not edit the predefined function name
    train = read_train_data()
    # Check for null values using the isnull() method and sum them for each column
    return train.isnull().sum()

# NA values in test dataset

def check_null_values_test():
    # do not edit the predefined function name
    test = read_test_data()
    # Check for null values using the isnull() method and sum them for each column
    return test.isnull().sum()



def filling_values_train():
    # do not edit the predefined function name
    train = read_train_data()

    # Fill missing values in the 'Bed Grade' column with the most frequent value (mode)

    # Replace missing values in the 'City_Code_Patient' column with the most frequent value (mode)
    train["Bed Grade"] = train["Bed Grade"].fillna(int(train["Bed Grade"].mode()))
    train["City_Code_Patient"] = train["City_Code_Patient"].fillna(int(train["City_Code_Patient"].mode()))
    #Return the updated 'train' DataFrame with missing values filled
    return train


def filling_values_test():
    # do not edit the predefined function name
    test = read_test_data()

    # Fill missing values in the 'Bed Grade' column with the most frequent value (mode)

    # Fill missing values in the 'City_Code_Patient' column with the most frequent value (mode)
    test["Bed Grade"] = test["Bed Grade"].fillna(int(test["Bed Grade"].mode()))
    test["City_Code_Patient"] = test["City_Code_Patient"].fillna(int(test["City_Code_Patient"].mode()))
    # SReturn the updated 'test' DataFrame with missing values filled
    return test




