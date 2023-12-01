import numpy as np
import pandas as pd

np.random.seed(42)
pd.set_option('mode.chained_assignment', None)
# Label Encoding Stay column in train dataset
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

def label_encoding():
    # do not edit the predefined function name
    train = filling_values_train()

    # Perform label encoding on the 'Stay' column
    lee = le.fit(train["Stay"])
    train["Stay"] = lee.transform(train["Stay"])
    # Return the updated 'train' DataFrame with the 'Stay' column label-encoded
    return train




#Imputing dummy Stay column in test datset to concatenate with train dataset
def dummy_column():
    # do not edit the predefined function name
    test = filling_values_test()

    # Set a dummy value (-1) for the 'Stay' column in the 'test' DataFrame
    test["Stay"] = -1
    # Return the updated 'test' DataFrame with the 'Stay' column set to the dummy value
    return test



def concat():
    # do not edit the predefined function name
    train = label_encoding()
    test = dummy_column()
    df = pd.DataFrame(columns=train.columns)

    # Concatenate the 'train' and 'test' DataFrames along rows, ignoring their original indexes
    df = pd.concat(train,test,ignore_index=True,axis=0)

    # Return the concatenated DataFrame
    return df

def label_encoding_df():
    # do not edit the predefined function name
    df = concat()

    # Perform label encoding on selected categorical columns ('Hospital_type_code', 'Hospital_region_code', 'Department', 'Ward_Type', 'Ward_Facility_Code', 'Type of Admission', 'Severity of Illness', 'Age')
    for i in df[['Hospital_type_code', 'Hospital_region_code', 'Department', 'Ward_Type', 'Ward_Facility_Code', 'Type of Admission', 'Severity of Illness', 'Age']]:
        mod = le.fit(df[i])
        df[i] = mod.transform(df[i])

    # Return the updated DataFrame with label-encoded categorical columns
    return df
