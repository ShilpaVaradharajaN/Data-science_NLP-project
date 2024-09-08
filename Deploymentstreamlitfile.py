import streamlit as st
from textblob import TextBlob
from streamlit_extras.let_it_rain import rain

st.title(" Sentiment Analysis App.")

message = st.text_area("Please Enter The Review")

if st.button("Analyze the Sentiment"):
    if message.strip():  # Check if the text area is not empty
        blob = TextBlob(message)
        result = blob.sentiment
        polarity = result.polarity

        if polarity < 0:
            st.warning(f"The entered text has negative sentiments associated with it: {polarity}")
            
        elif polarity > 0:
            st.success(f"The entered text has positive sentiments associated with it: {polarity}")
            
        else:
            st.info("The entered text seems to be neutral.")

        st.success(f"Sentiment Analysis Result: {result}")
    else:
        st.warning("Please enter some text to analyze.")
