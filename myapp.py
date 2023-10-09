import streamlit as st
from textblob import TextBlob
import emoji

# Function for sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    return sentiment

# Streamlit app title
st.title("Sentiment Analysis Chatbot")

# User input for comments
user_comment = st.text_area("Enter your comment:")

# Explanation of sentiment score
st.write("Sentiment Score Explanation:")
st.write("- A positive score indicates a positive sentiment.")
st.write("- A negative score indicates a negative sentiment.")
st.write("- A score near zero suggests a neutral sentiment.")

# "RUN" button to trigger sentiment analysis
if st.button("RUN"):
    if user_comment:
        sentiment = analyze_sentiment(user_comment)
        st.write(f"**Sentiment Score:** {sentiment:.2f}")
        
        # Determine the emoji based on sentiment score
        if sentiment > 0.5:
            emoji_icon = emoji.emojize(":grinning_face_with_big_eyes:")
        elif sentiment < -0.5:
            emoji_icon = emoji.emojize(":disappointed_face:")
        else:
            emoji_icon = emoji.emojize(":neutral_face:")
        
        st.write(f"**Sentiment Emoji:** {emoji_icon}")

        # Display sentiment-related animation (you can replace this with your own animations)
        if sentiment > 0.5:
            st.video('https://example.com/happy_animation.mp4')  # URL to a happy animation
        elif sentiment < -0.5:
            st.video('https://example.com/sad_animation.mp4')  # URL to a sad animation
        else:
            st.video('https://example.com/neutral_animation.mp4')  # URL to a neutral animation
