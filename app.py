import streamlit as st
from summarizer import summarize_text

st.title("📝 AI Text Summarizer")

st.write("Enter a paragraph below and get a concise AI-generated summary.")

text = st.text_area(
    "Text to summarize",
    height=200
)

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        summary = summarize_text(text)

        st.subheader("Summary")
        st.write(summary)