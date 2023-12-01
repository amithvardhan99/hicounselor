
import pandas as pd


import warnings
warnings.filterwarnings('ignore')

# The dataset being used is the **sentiment140 dataset**. It contains tweets extracted using the **Twitter API**. The tweets have been annotated **(0 = Negative, 4 = Positive)** and they can be used to detect sentiment.

#
# **It contains the following 6 fields:**
# 1. **sentiment**: the polarity of the tweet *(0 = negative, 4 = positive)*
# 2. **ids**: The id of the tweet *(2087)*
# 3. **date**: the date of the tweet *(Sat May 16 23:58:44 UTC 2009)*
# 4. **flag**: The query (lyx). If there is no query, then this value is NO_QUERY.
# 5. **user**: the user that tweeted *(robotickilldozr)*
# 6. **text**: the text of the tweet *(Lyx is cool)*
#
# We require only the **sentiment** and **text** fields, so we discard the rest.
#
# Furthermore, we're changing the **sentiment** field so that it has new values to reflect the sentiment. **(0 = Negative, 1 = Positive)**

# In[ ]:
# Importing the dataset
def load_dataset():
    #use dataset encoding while reading the data
    DATASET_ENCODING = "ISO-8859-1"
    dataset = pd.read_csv("Sentiment_data.csv",encoding=DATASET_ENCODING)
    return dataset


# Removing the unnecessary columns.
def pre_processing():
    #do not remove the predefined function
    df = load_dataset()
    #Use Sentiment and text column
    # Replacing the values to ease understanding(replace 4 from 1).
    df_1 = df[["sentiment","text"]]
    y = lambda x:1 if x==4 else 0
    v = map(y,df_1["sentiment"])
    df_1["sentiment"] = pd.Series(list(v))
    return df_1


# Plotting the distribution for dataset.
def plot_distribution():
    #do not remove the predefined function
    df_1 = pre_processing()
    #here return the count of different values in sentiment hence use groupby function and count it
    h = df_1.groupby("sentiment")
    grp = h.groups
    dic = dict()
    for i in grp:
        dic[i] = len(grp[i])
    df_2 = pd.DataFrame(columns=["sentiment","text"])
    df_2["sentiment"] = dic.keys()
    df_2["text"] = dic.values()
    df_2 = df_2.set_index(df_2["sentiment"],inplace=False)
    df_2 = df_2.drop("sentiment",axis=1,inplace=False)
    # plt.show()
    return df_2


# Storing data in lists.
def store_data():
    #do not remove the predefined function
    df_1 = pre_processing()
    #Here split the dataset for text and sentiment and return it.
    text = list(df_1["text"])
    sentiment = list(df_1["sentiment"])
    return text, sentiment


