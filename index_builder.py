import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch.helpers import bulk

df = pd.read_csv("/home/harish/final_project/index_dataset.csv")

def create_dict(set):
    headline = list(df["TITLE"])
    url = list(df["URL"])
    cat = list(df["CATEGORY"])
    prob = list(df["PROBABILITY"])
    index_list = []
    for i in range(len(df)):
        dct_obj = dict(headline=headline[i], url=url[i], category=cat[i], probability=prob[i])
        index_list.append(dct_obj)
    return index_list

es = Elasticsearch()
index_instance = IndicesClient(es)
mapping_dct = {"mappings":{"newspaper_articles":{"properties":{"headline":{"type":"string","analyzer":"standard"},"url":{"type":"string"},"category":{"type":"string","analyzer":"standard"},"probability":{"type":"integer"}}}}}
index_instance.create(index="article_index", body=mapping_dct)
body = create_dict(df)
ACTIONS = []
for elem in body:
    action = {
        "_index": "article_index",
        "_type": "newspaper_articles",
        "_source": {
            "headline": elem["headline"],
            "url": elem["url"],
            "category":elem["category"],
            "probability":elem["probability"]
        }
    }
    ACTIONS.append(action)
bulk(es, ACTIONS, index = "article_index")
