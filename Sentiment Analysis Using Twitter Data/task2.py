import numpy as np
import pandas as pd
import task1 as t
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import *
from sklearn import preprocessing
import warnings
warnings.filterwarnings('ignore')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.casual import TweetTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
import re
import nltk
import string
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

def preprocess():

    text,sentiment = t.store_data()

    emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad',
              ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
              ':-@': 'shocked', ':@': 'shocked', ':-$': 'confused', ':\\': 'annoyed',
              ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
              '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
              '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink',
              ';-)': 'wink', 'O:-)': 'angel', 'O*-)': 'angel', '(:-D': 'gossip', '=^.^=': 'cat'}

    stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
                    'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before',
                    'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do',
                    'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
                    'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
                    'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
                    'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
                    'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once',
                    'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'own', 're',
                    's', 'same', 'she', "shes", 'should', "shouldve", 'so', 'some', 'such',
                    't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
                    'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
                    'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
                    'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
                    'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre",
                    "youve", 'your', 'yours', 'yourself', 'yourselves']

    stopwords = set(stopwordlist)

    def emoji_replace(text,emojis):
        for i in emojis.keys():
            while i in text:
                text = text.replace(i,"EMOJI"+emojis[i])
        return text

    def alpha_replace(text,alphaPattern):
        w = text.split()
        res = []
        for i in w:
            p = re.sub(alphaPattern,"",i)
            if len(p)>0:
                res.append(p)
        s = " ".join(res)
        return s

    def word_lemmatize(text):
        wl = WordNetLemmatizer()
        w = text.split()
        res = []
        for i in w:
            res.append(wl.lemmatize(i))
        s = " ".join(res)
        return s

    def remove_stopwords(text,stopwords):
        w = text.split()
        res = []
        for i in w:
            if i not in stopwords:
                res.append(i)
        s = " ".join(res)
        return s

    urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern = '@[^\s]+'
    alphaPattern = "[^a-zA-Z0-9]"
    sequencePattern = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"

    final_text = []

    for i in text:
        tb = i.lower()
        tb = re.sub(urlPattern,"URL",tb)
        tb = emoji_replace(tb,emojis)
        tb = re.sub(userPattern,"USER",tb)
        tb = alpha_replace(tb,alphaPattern)
        tb = re.sub(sequencePattern,seqReplacePattern,tb)
        tb = word_lemmatize(tb)
        tb = remove_stopwords(tb,stopwords)
        final_text.append(tb)


    return final_text