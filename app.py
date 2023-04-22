import spacy
from string import punctuation
import streamlit as st
import re
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest


@st.cache_data
def preprocessing(inp_str):
    inp = nlp(inp_str)
    word_count = {}
    for word in inp:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_count.keys():
                word_count[word.text] = 1
            else:
                word_count[word.text] += 1
    max_count = max(word_count.values())

    for word in word_count.keys():
        word_count[word] = word_count[word] / max_count

    sentence_list = [sent for sent in inp.sents]

    sentences_count = {}
    for sent in sentence_list:
        for word in sent:
            if word.text in word_count.keys():
                if sent not in sentences_count.keys():
                    sentences_count[sent] = word_count[word.text]
                else:
                    sentences_count[sent] += word_count[word.text]
    select_len = int(len(sentence_list) * 0.3)
    summary = nlargest(select_len, sentences_count, key=sentences_count.get)
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)
    return summary


stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


st.title(" Text Summarizer ")

input = st.text_area("Enter your Text :", height=200)


button = st.button("Summarize")


with st.spinner("Generating Summary.."):
    if button and input:
        res = preprocessing(input)
        st.write(res)
        st.write("Length: ", len(res.split()))
