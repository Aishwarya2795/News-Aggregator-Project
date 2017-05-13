from elasticsearch import Elasticsearch
es = Elasticsearch()
while(1):
    print("Would you like to search by:\n(1)Keyword\n(2)Category\n(3)Exit\n")
    choice = input()
    if choice == "1":
        print("Enter keywords to search\n")
        body = input()
        dct = {"query":{"match":{"headline":body}}}
        res = es.search(index="article_index",doc_type="newspaper_articles",body=dct)
        res_hits = res["hits"]["hits"]
        if len(res_hits) == 0:
            print("No results")
        for elem in res_hits:
            print(elem["_source"]["headline"],"\n",elem["_source"]["url"],"\n",elem["_source"]["category"])
    elif choice == "2":
        print("Enter category to search.\nYour options are:\nb\ne\nm\nt\n")
        body = input()
        dct = {"query":{"match":{"category":body}}}
        res = es.search(index="article_index", doc_type="newspaper_articles", body=dct)
        res_hits = res["hits"]["hits"]
        if len(res_hits) == 0:
            print("No results")
        for elem in res_hits:
            print(elem["_source"]["headline"], "\n", elem["_source"]["url"], "\n", elem["_source"]["category"])
    else:
        break