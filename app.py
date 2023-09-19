import streamlit as st
import pyshorteners

def index(url):
    
    
        
        s=pyshorteners.Shortener()
        output=s.tinyurl.short(url)
        return output
#@st.cache
st.title("URL SHORTENER")
st.header("Enter short URL:")

url=st.text_input("URL")
if st.button('SUBMIT'):
    s=index(url)
    st.success(f'Shortened URL: {s} ')