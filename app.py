import streamlit as st
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

st.set_page_config(page_title='URL Shortener', page_icon='https://icon-library.com/images/code-icon-png/code-icon-png-5.jpg')
st.title(" 🔗 URL Shortener")
st.markdown("<a href='https://github.com/deepraj21'><img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white' alt='GitHub'></a>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

url = st.text_input("Enter the URL:")

if st.button("Shorten"):
    if url:
        shortened = shorten_url(url)
        st.success("Shortened URL: {}".format(shortened))
    else:
        st.warning("Please enter a valid URL.")
