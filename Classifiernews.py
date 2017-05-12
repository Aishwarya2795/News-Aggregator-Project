
import numpy as np
import pandas as pd
import re
import string
from tkinter import *
# import matplotlib.pyplot as plt

# the Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
# function to split the data for cross-validation
from sklearn.model_selection import train_test_split
# function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer
# function for encoding categories
from sklearn.preprocessing import LabelEncoder

def comp():
    column_names= ['ID','TITLE','URL','PUBLISHER','CATEGORY','STORY','HOSTNAME','TIMESTAMP']
    news_df = pd.read_csv('newsCorpora.csv',sep='	',names=column_names)
    X_independent = pd.DataFrame(news_df.iloc[1:5,:2].values)
    X_independent = news_df.iloc[:,:2].values
    headline = list(news_df["TITLE"])
    headline1 = []
    for elem in headline:
        s = elem.lower()
        trans = str.maketrans("","",string.punctuation)
        s = s.translate(trans)
        headline1.append(s)
    news_df["FORM_HEADLINE"] = headline1
    X_independent = news_df[["ID","FORM_HEADLINE"]]
    Y_dependent = news_df["CATEGORY"]
    encoder = LabelEncoder()
    Y_dependent = encoder.fit_transform(Y_dependent)
    vec = CountVectorizer()
    x = vec.fit_transform(news_df["FORM_HEADLINE"])
    x_train, x_test, y_train, y_test = train_test_split(x, Y_dependent, test_size=0.2)
    nb = MultinomialNB()
    nb.fit(x_train, y_train)
    scr = nb.score(x_test,y_test)
    print(scr*100)
    x1 = x_test[:3,:]
    h = list(news_df.iloc[1000:1003,8])
    test1 = vec.transform(h)
    y = nb.predict(test1)
    t1.insert(END,y)
    return(y,scr*100)
