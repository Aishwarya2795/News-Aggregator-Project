from tkinter import *
from Classifiernews import *

window=Tk()

def predictor():
    cat,acc=comp()
    t1.insert(END,cat)

def accuracy():
    cat,acc=comp()
    t2.insert(END,acc)


b1=Button(window,text="CLICK THIS TO GET PREDICTED CATEGORY",command=predictor)
b1.grid(row=0,column=0)


b2=Button(window,text="CLICK THIS TO GET ACCURACY RATE",command=accuracy)
b2.grid(row=3,column=0)


t1=Text(window,height=5,width=20)
t1.grid(row=2,column=0)
t2=Text(window,height=5,width=20)
t2.grid(row=5,column=0)

window=mainloop()
ain_test_split(x, Y_dependent, test_size=0.2)
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

def accuracy():
    cat,acc=comp()
    t2.insert(END,scr*100)
    

b1=Button(window,text="CLICK THIS TO GET PREDICTED CATEGORY",command=comp)
b1.grid(row=0,column=0)


b2=Button(window,text="CLICK THIS TO GET ACCURACY RATE",command=accuracy)
b2.grid(row=2,column=0)

t1=Text(window,height=5,width=20)
t1.grid(row=1,column=0)
t2=Text(window,height=5,width=20)
t2.grid(row=3,column=0)

window=mainloop()
