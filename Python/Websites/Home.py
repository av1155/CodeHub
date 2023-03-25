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
st.image(logo, width=500)
st.title("Python Learning Resources")

# Define the description section
st.write("Welcome to the Python Learning Resources website! Here you will find a curated list of resources to help you learn Python. Use the navigation bar on the left to explore the different sections of the website.")
st.write("To get started, we recommend checking out the SoloLearn section for free coding courses or the Python Resources section for tutorials and articles on Python programming.")
