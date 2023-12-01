import task4 as t4
import re
import pickle
import numpy as np
import pandas as pd

# plotting
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# nltk
from nltk.stem import WordNetLemmatizer

# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

import warnings
warnings.filterwarnings('ignore')



# BernoulliNB Model

def bnb_model_Evaluate():
    # Predict values for Test dataset
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = t4.split_data()
    X_train, X_test = t4.vectoriser_fit_and_tranfer_data()
    BNBmodel = BernoulliNB(alpha=2)
    model = BNBmodel.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    rep = classification_report(y_test,y_pred)
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test,y_pred)


    return rep







# LinearSVC Model
def svc_model_Evaluate():
    # Predict values for Test dataset
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = t4.split_data()
    X_train, X_test = t4.vectoriser_fit_and_tranfer_data()
    SVCmodel = LinearSVC()
    model = SVCmodel.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    rep = classification_report(y_test,y_pred)
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test,y_pred)


    return rep







#Logistic Regression Model

def lr_model_Evaluate():
    # Predict values for Test dataset
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = t4.split_data()
    X_train, X_test = t4.vectoriser_fit_and_tranfer_data()
    LRmodel = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
    model = LRmodel.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    rep = classification_report(y_test,y_pred)
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test,y_pred)
    return rep

def lr_model():
    # Predict values for Test dataset
    #do not remove the predefined function
    X_train, X_test, y_train, y_test = t4.split_data()
    X_train, X_test = t4.vectoriser_fit_and_tranfer_data()
    LRmodel = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
    model = LRmodel.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    rep = classification_report(y_test,y_pred)
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test,y_pred)
    return LRmodel

