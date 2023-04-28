# text-summarizer
This Project provides a simple and easy-to-use web application for text summarization, and demonstrates the use of Spacy for NLP preprocessing and Streamlit for building interactive web applications.
# Preprocessing
Tokenizing any given input string using Spacy.
Counts the occurrence of each non-stopword and non-punctuation word in the input.
Normalizes the word counts by dividing each count by the maximum count.
Splits the input into sentences and computes a score for each sentence by summing the normalized word counts for each word in the sentence.
Selects the top 30% of sentences based on their score, and concatenates them into a final summary.
# WebApp
Streamlit application is used tp  provide a simple user interface for text summarization where the user enters a text in the text area and the resulting summary is generated.
