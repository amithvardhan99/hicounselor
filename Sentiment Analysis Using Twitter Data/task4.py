import task2 as t2
import task1 as t1



from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


import warnings
warnings.filterwarnings('ignore')




def split_data():
    #do not remove the predefined function
    processedtext = t2.preprocess()
    text, sentiment = t1.store_data()
    X_train, X_test, y_train, y_test = train_test_split(processedtext,sentiment,test_size=0.05,random_state=0)
    return X_train, X_test, y_train, y_test


#TF-IDF Vectoriser
# **TF-IDF indicates what the importance of the word is in order to understand the document or dataset.** Let us understand with an example. Suppose you have a dataset where students write an essay on the topic, My House. In this dataset, the word a appears many times; it’s a high frequency word compared to other words in the dataset. The dataset contains other words like home, house, rooms and so on that appear less often, so their frequency are lower and they carry more information compared to the word. This is the intuition behind TF-IDF.
#
# **TF-IDF Vectoriser** converts a collection of raw documents to a **matrix of TF-IDF features**. The **Vectoriser** is usually trained on only the **X_train** dataset.
#
# **ngram_range**  is the range of number of words in a sequence. *[e.g "very expensive" is a 2-gram that is considered as an extra feature separately from "very" and "expensive" when you have a n-gram range of (1,2)]*
#
# **max_features** specifies the number of features to consider. *[Ordered by feature frequency across the corpus]*.

# In[ ]:

def vectoriser_fit_and_tranfer_data():
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = split_data()
    vectoriser = TfidfVectorizer(ngram_range=(1,2),max_features=10000)
    model = vectoriser.fit(X_train,y_train)
    X_train = model.transform(X_train)
    X_test = model.transform(X_test)

    return X_train, X_test

def vectoriser():
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = split_data()
    vectoriser = TfidfVectorizer(ngram_range=(1,2),max_features=10000)
    model = vectoriser.fit(X_train,y_train)
    X_train = model.transform(X_train)
    X_test = model.transform(X_test)

    return vectoriser



