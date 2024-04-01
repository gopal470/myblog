# Import necessary libraries
import streamlit as st

# Set page config
st.set_page_config(page_title='Gopala Krishnan Ramanadar Blog', page_icon=':memo:', layout='centered')

def main():
    st.title("Welcome to Gopala Krishnan Ramanadar's Blog")
    st.subheader('Software Engineer at eBay Inc.')
    
    st.write("""
    Hello and welcome! My name is Gopala Krishnan Ramanadar, and I'm a software engineer with 20 years of industry experience, 
    currently working at eBay Inc. Here, on my blog, I share my insights, experiences, and thoughts on the dynamic landscape of software engineering. 
    My aim is to help like-minded professionals and enthusiasts navigate the fascinating world of software development. 
    Enjoy your stay and don't hesitate to reach out if you have any questions or discussions in mind. Happy reading!
    """)

if __name__ == "__main__":
    main()
