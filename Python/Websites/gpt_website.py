import streamlit as st

# Define a function for each resource link


def resource_link(name, url):
    st.write(f"[{name}]({url})")


# Define the layout of the page
st.set_page_config(page_title="Python Resources", page_icon=":snake:")
st.title("Python Resources")
st.header("Basic Learning")

# Add the links to each resource
resource_link("SoloLearn", "https://www.sololearn.com/")
resource_link("Python Documentation", "https://docs.python.org/3/")
resource_link("Python Tutorial", "https://www.learnpython.org/")
resource_link("Python for Everybody", "https://www.py4e.com/")
resource_link("Codecademy", "https://www.codecademy.com/learn/learn-python")
resource_link("Real Python", "https://realpython.com/")

# Add a footer with your name and contact information
st.markdown("---")
st.write("Created by Your Name")
st.write("Contact me at your.email@example.com")
