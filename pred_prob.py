from classifier import vec, news_df
import pickle
import os
nb = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))
headlines = list(news_df["TITLE"])
prob = []
for headline in headlines:
    sub = vec.transform([headline])
    x = nb.predict_proba(sub)
    prob.append(max(x[0]))
news_df["PROBABILITY"] = prob
news_df.to_csv("/home/harish//final_project/index_dataset.csv")