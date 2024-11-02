

import string
import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Function to process and clean text
def preprocess_text(text):
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = word_tokenize(cleaned_text, "english")
    final_words = [word for word in tokenized_words if word not in stopwords.words('english')]
    lemma_words = [WordNetLemmatizer().lemmatize(word) for word in final_words]
    return lemma_words

# Function to analyze emotions in the text
def analyze_emotions(lemma_words):
    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in lemma_words:
                emotion_list.append(emotion)
    return Counter(emotion_list)

# Function to analyze sentiment
def sentiment_analyse(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    if score['neg'] > score['pos']:
        return "Negative Sentiment"
    elif score['neg'] < score['pos']:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment"

# Streamlit application setup
st.title("Sentiment Analysis Chatbot")
st.write("Enter text below to analyze its sentiment and emotions.")

# Text input box
user_text = st.text_area("Enter Text Here", height=150)

# Predict button
if st.button("Predict"):
    if user_text:
        lemma_words = preprocess_text(user_text)
        emotion_counts = analyze_emotions(lemma_words)
        
        # Display sentiment result
        sentiment_result = sentiment_analyse(user_text)
        st.subheader("Sentiment Result:")
        st.write(sentiment_result)
        
        # Plot and display emotion counts
        if emotion_counts:
            fig, ax = plt.subplots()
            ax.bar(emotion_counts.keys(), emotion_counts.values())
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.write("No emotion words found in the text.")
    else:
        st.write("Please enter some text to analyze.")





