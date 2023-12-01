
import task1 as t1
import task2 as t2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# do not remove the predefined function
processedtext = t2.preprocess()



#Word-Cloud for Negative tweets.
def negative_tweets_wordcloud():
    #slice the initial 10000 text from processedtext for negative tweets
    processedtext = t2.preprocess()
    negative_tweets = processedtext[0:10000]
    words = ""
    for i in negative_tweets:
        words += (i + " ")
    wc = WordCloud(max_words=10000,width=1000,height=1000,collocations=True)
    word_cloud = wc.generate(words)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.show()

    # plt.show()
    return negative_tweets


#Word-Cloud for Positive tweets.
def positive_tweets_wordcloud():
    #slice the after 10000 text from processedtext for negative tweets
    processedtext = t2.preprocess()
    positive_tweets = processedtext[10000:]
    words = ""
    for i in positive_tweets:
        words += (i + " ")
    wc = WordCloud(max_words=10000,width=1000,height=1000,collocations=True)
    word_cloud = wc.generate(words)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.show()

    # plt.show()
    return positive_tweets


