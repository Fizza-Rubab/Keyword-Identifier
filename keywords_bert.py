import time
from keybert import KeyBERT
import re

def pre_process(text):
    text=text.lower()
    text=re.sub("</?.*?>"," <> ",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    return text

def get_keywords(text):
    clean_text = pre_process(text)
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(clean_text)
    print(keywords)
    return ' '.join([i[0] for i in keywords])


if __name__=="__main__":
    doc = """Tables, panels, consoles, drawers, cabinets and other media containing more than a device of heading 85.35 or 85.36, for electrical control or distribution, including those containing instruments or devices of heading 90, as well as numerical control devices, other than switching devices of heading 85.17, with a voltage not exceeding 1000 V"""
    t = time.time()
    kw_model = KeyBERT()
    keywords = get_keywords(doc)
    print(keywords)
    print("Time elapsed:", time.time()-t)
