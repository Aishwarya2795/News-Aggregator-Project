import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
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
for elem in body:
    es.index(index="article_index", doc_type="newspaper_articles", body=elem)