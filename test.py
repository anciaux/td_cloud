#!/usr/bin/env python
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title("EPFL Teaching Day 2023: word cloud")


_file = st.file_uploader('Upload your text file here')
if _file is not None:
    comment_words = ''
    stopwords = set(STOPWORDS)
    text = _file.read().decode()
    text = text.replace('\n', ' ')
    text = text.split()
    text = [e.lower().strip() for e in text]

    comment_words = " ".join(text)

    wordcloud = WordCloud(width=1500, height=int(1500*9/16),
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    fig = plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig)
