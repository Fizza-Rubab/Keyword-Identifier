import re
import pandas as pd
import pickle
from time import time

def pre_process(text):
    text=text.lower()
    text=re.sub("</?.*?>"," <> ",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    text = ' '.join( [w for w in text.split() if len(w)>1] )
    return text

def get_keywords(txt):
    doc = pre_process(txt)
    with open("tfidfvectorize_result.pkl", 'rb') as handle:
        vectorizer = pickle.load(handle)
    tf_idf_vector=vectorizer.transform([doc])
    dfn = pd.DataFrame(tf_idf_vector.T.todense(), index=vectorizer.get_feature_names_out(), columns=["tfidf"])
    x = (dfn.sort_values(by=["tfidf"], ascending=False)[:5])
    print(x)
    return ' '.join(x.index.to_list())


if __name__=="__main__":
    st = time()
    result = get_keywords("MEMPHIS/EASTERN 2022/2023 CROP UPLAND COTTON USDA HVI CLASS: 42/51-4-36 AND LONGER MIKE:4.0-5.2 NCL GPT:: 28.0 MIN")
    et = time()
    print(f"Elapsed time {et-st}")
    print(f"Keywords Obtained: {result}")