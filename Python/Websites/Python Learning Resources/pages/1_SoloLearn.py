# Import the required libraries
import streamlit as st

# Set the title of the website
st.set_page_config(
    page_title="SoloLearn",
    page_icon=":snake:",
    layout="wide",
)

# Define the logo
logo = "https://blob.sololearn.com/avatars/sololearn.png"

# Add the logo and title to the website
st.image(logo, width=125)
st.title("SoloLearn")

st.write("SoloLearn is a mobile and web-based platform that offers free coding courses in various programming languages, including Python.")
st.write("Click the link below to visit the SoloLearn website:")
st.write("- [SoloLearn](https://www.sololearn.com/)")
