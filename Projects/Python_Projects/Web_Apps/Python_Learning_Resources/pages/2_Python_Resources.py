# Import the required libraries
import streamlit as st

# Set the title of the website
st.set_page_config(
    page_title="Python Resources",
    page_icon=":snake:",
    layout="wide",
)

# Define the logo
logo = "https://miro.medium.com/v2/resize:fit:1200/1*WWrXceae4H_klzpPU6h7Hg.png"

# Add the logo and title to the website
st.image(logo, width=250)
st.title("Python Resources")

st.write("Here are some resources to help you learn Python:")
st.write(
    "- [Python Documentation](https://docs.python.org/3/): The official Python documentation.")
st.write(
    "- [Real Python](https://realpython.com/): Tutorials and articles on Python programming.")
st.write(
    "- [Python Central](https://www.pythoncentral.io/): A collection of Python resources.")
st.write(
    "- [Python Weekly](https://www.pythonweekly.com/): A weekly newsletter for Python developers.")
st.write(
    "- [Python Tutor](http://pythontutor.com/): A tool for visualizing Python code execution.")
st.write(
    "- [Python Anywhere](https://www.pythonanywhere.com/): A cloud-based Python development environment.")
