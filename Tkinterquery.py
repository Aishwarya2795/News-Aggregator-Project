from elasticsearch import Elasticsearch
from tkinter import *
es = Elasticsearch()

window = Tk()
    #print("Would you like to search by:\n(1)Keyword\n(2)Category\n(3)Exit\n")
    #choice = input()
    #if choice == "1":


def keywords():
    #list_keys["ta1"].insert(END,"HELLLO THIS THIS WORKING" )
        #print("Enter keywords to search\n")
        #body = input()
        body = body1.get()
        dct = {"query":{"match":{"headline":body}}}
        res = es.search(index="article_index",doc_type="newspaper_articles",body=dct)
        res_hits = res["hits"]["hits"]
        count = 1
        if len(res_hits) == 0:
            #print("No results")
            ta1.insert(END,"NO RESULTS")
            ta2.insert(END,"NO RESULTS")
            ta3.insert(END,"NO RESULTS")
        else:
            for elem in res_hits:
            #print(elem["_source"]["headline"],"\n",elem["_source"]["url"],"\n",elem["_source"]["category"])
            #ta1.insert(END,elem["_source"]["headline"])
            #ta2.insert(END,elem["_source"]["url"])
            #ta3.insert(END,elem["_source"]["category"])
                list_keys["ta{}".format(count)].insert(END,elem["_source"]["headline"]) )
                count = count + 1
                list_keys["ta{}".format(count)].insert(END,elem["_source"]["url"]) )
                count = count + 1
                list_keys["ta{}".format(count)].insert(END,elem["_source"]["url"]) )
                count = count + 1




    #elif choice == "2":
def categories():
    print("HI")
        #print("Enter category to search.\nYour options are:\nb\ne\nm\nt\n")
        #body = input()
        body = body2.get()
        dct = {"query":{"match":{"category":body}}}
        res = es.search(index="article_index", doc_type="newspaper_articles", body=dct)
        res_hits = res["hits"]["hits"]
        if len(res_hits) == 0:
            #print("No results")
            ta1.insert(END,"NO RESULTS")
            ta2.insert(END,"NO RESULTS")
            ta3.insert(END,"NO RESULTS")
        count = 1
        for elem in res_hits:
            #print(elem["_source"]["headline"], "\n", elem["_source"]["url"], "\n", elem["_source"]["category"])
            list_keys["ta{}".format(count)].insert(END,elem["_source"]["headline"]) )
            count = count + 1
            list_keys["ta{}".format(count)]..insert(END,elem["_source"]["url"]) )
            count = count + 1
            list_keys["ta{}".format(count)].insert(END,elem["_source"]["url"]) )
            count = count + 1
#    else:
#break



def clear_entry_fields():
   e1.delete(0,END)
   e2.delete(0,END)
   for x in range(1,16):
       list_keys["ta{}".format(x)].delete(1.0,END)



l1=Label(window,text="Keywords",height=5,width=8)
l1.grid(row=0,column=0)
body1=StringVar()
e1=Entry(window,textvariable=body1)
e1.grid(row=0,column=1)  #Entry of the Keywords
b1=Button(window,text="SEARCH",command=keywords)
b1.grid(row=0,column=2)

l2=Label(window,text="Category",height=5,width=8)
l2.grid(row=1,column=0)
body2=StringVar()
e2=Entry(window,textvariable=body2)
e2.grid(row=1,column=1)  #Entry of the Keywords
b2=Button(window,text="SEARCH",command=categories)
b2.grid(row=1,column=2)
#Clear Button
b4=Button(window,text="CLEAR ALL",command=clear_entry_fields)
b4.grid(row=11,column=1)

Headline_Label=Label(window,text="Headline",height=5,width=8)
Headline_Label.grid(row=2,column=0)
Url_Label=Label(window,text="URL",height=5,width=8)
Url_Label.grid(row=2,column=1)
Category_Label=Label(window,text="Category",height=5,width=8)
Category_Label.grid(row=2,column=2)


row_no = 4
list_keys = {}
for x in range(1,16,3):
        for y in range(0,3):
            list_keys.update({"ta{}".format(x) : Text(window,height=5,width=30)})
            list_keys["ta{}".format(x)].grid(row = row_no, column = y)
            x=x+1
        row_no = row_no + 1

"""


ta1=Text(window,height=5,width=30)
ta1.grid(row=2,column=0) #Headline output
ta2=Text(window,height=5,width=30)
ta2.grid(row=2,column=1) #URL output
ta3=Text(window,height=5,width=30)
ta3.grid(row=2,column=2) #Category output
ta4=Text(window,height=5,width=30)
ta4.grid(row=3,column=0) #Headline output
ta5=Text(window,height=5,width=30)
ta5.grid(row=3,column=1) #URL output
ta6=Text(window,height=5,width=30)
ta6.grid(row=3,column=2) #
ta7=Text(window,height=5,width=30)
ta7.grid(row=4,column=0) #Headline output
ta8=Text(window,height=5,width=30)
ta8.grid(row=4,column=1) #URL output
ta9=Text(window,height=5,width=30)
ta9.grid(row=4,column=2)
ta10=Text(window,height=5,width=30)
ta10.grid(row=5,column=0) #Headline output
ta11=Text(window,height=5,width=30)
ta11.grid(row=5,column=1) #URL output
ta12=Text(window,height=5,width=30)
ta12.grid(row=5,column=2) #
ta13=Text(window,height=5,width=30)
ta13.grid(row=6,column=0) #Headline output
ta14=Text(window,height=5,width=30)
ta14.grid(row=6,column=1) #URL output
ta15=Text(window,height=5,width=30)
ta15.grid(row=6,column=2) #

"""


window = mainloop()
