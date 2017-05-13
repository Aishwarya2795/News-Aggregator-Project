from tkinter import *
from Classifiernewscopy import *
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import re
import string

#import cPickle
# import matplotlib.pyplot as plt

# the Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
# function to split the data for cross-validation
from sklearn.model_selection import train_test_split
# function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer
# function for encoding categories
from sklearn.preprocessing import LabelEncoder

window=Tk()
"""
def predictor():
    nb,vec,acc=comp()
    t1.insert(END,cat)
"""

def accuracy():

    nb,vec,acc=comp()
    acc = int(acc)
    acc = "Prediction Accuracy Rate --> {}%".format(acc)
    t2.insert(END,acc)


def enter_headline():
    filename = '/tmp/vec_classifier.joblib.pkl'
    vec = joblib.load('/tmp/vec_classifier.joblib.pkl')
    #nb = joblib.load('newsname.pkl')
    nb_loaded = joblib.load('/tmp/nb_classifier.joblib.pkl')
    #nb,acc=comp()
    test2=test1.get()
    test3=[test2] #pass test1 as an element into test2 list to do the vec transform
    test4 = vec.transform(test3)
    predicted_category = nb_loaded.predict(test4)
    a = [0,1,2,3]
    count = 0
    for p in predicted_category:
        if p==0:
            val = "BUSINESS AND FINANCE"
        elif p==1:
            val = "ENTERTAINMENT AND SPORTS"
        elif p==2:
            val ="     HEALTH"
        elif p==3:
            val ="   TECHNOLOGY"
        count=count+1
    t3.insert(END,val)


def clear_entry_fields():
   e1.delete(0,END)
   t3.delete(1.0, END)

b4=Button(window,text="CLEAR",command=clear_entry_fields)
b4.grid(row=11,column=0)

test1=StringVar()
e1=Entry(window,textvariable=test1)
e1.grid(row=8,column=0)

"""
b1=Button(window,text="CLICK THIS TO GET PREDICTED CATEGORY",command=predictor)
b1.grid(row=0,column=0)
"""

b2=Button(window,text="CLICK THIS TO GET ACCURACY RATE",command=accuracy)
b2.grid(row=1,column=0)

b3=Button(window,text="ENTER THE HEADLINE BELOW AND CLICK",command=enter_headline)
b3.grid(row=5,column=0)

t2=Text(window,height=5,width=30)
t2.grid(row=3,column=0)
t3=Text(window,height=5,width=30)
t3.grid(row=10,column=0)

window=mainloop()
