# Import the required libraries
import streamlit as st

# Set the title of the website
st.set_page_config(
    page_title="Python Learning Resources",
    page_icon=":snake:",
    layout="wide",
)

# Define the logo
logo = "https://logodownload.org/wp-content/uploads/2019/10/python-logo-3.png"

# Add the logo and title to the website
st.image(logo, width=400)
st.title("Python Learning Resources")

# Define the description section
st.write("Welcome to the Python Learning Resources website! Here you will find a curated list of resources to help you learn Python. Use the navigation bar on the left to explore the different sections of the website.")

st.write("This is your go-to website for learning and developing your Python programming skills. The SoloLearn page provides a website that offers an interactive learning platform, our Python Resources page includes curated resources to help you understand, our Python Video Tutorials page offers a structured learning experience with helpful videos from significant creators, and our Python Projects page offers you project ideas to challenge, engage, and assist you in expanding your portfolio. Explore our resources and tools to improve your proficiency in Python.")

# Define the footer section
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write("Connect with me:")
st.write(
    "[LinkedIn](https://www.linkedin.com/in/andrea-venti/)", " - ", "[GitHub](https://github.com/av1155)")
