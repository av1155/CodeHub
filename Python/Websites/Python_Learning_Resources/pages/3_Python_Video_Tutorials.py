# Import the required libraries
import streamlit as st

# Set the title of the website
st.set_page_config(
    page_title="SoloLearn",
    page_icon=":snake:",
    layout="wide",
)

# Define the logo
logo = "https://www.robinson-ries.com/wp-content/uploads/2018/12/youtube-icon-logo-png-512.png"

# Add the logo and title to the website
st.image(logo, width=125)
st.title("Python Video Tutorials")
st.write("Here are some short video tutorials to help you learn Python:")

st.write(
    "- [Python in 100 Seconds](https://youtu.be/x7X9w_GIm1s)")
st.write(
    "- [Python Tutorial Series](https://youtube.com/playlist?list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)")
st.write(
    "- [Python Habits to Avoid](https://youtu.be/qUeud6DvOWI)")
st.write(
    "- [Python Crash Course](https://youtu.be/JJmcL1N2KQs)")
st.write(
    "- [Python Full Course - Programming with Mosh](https://youtu.be/_uQrJ0TkZlc)")
st.write(
    "- [Python Full Course - freeCodeCamp](https://youtu.be/rfscVS0vtbw)")
