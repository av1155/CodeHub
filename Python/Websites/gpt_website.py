import streamlit as st

# Define a function for each resource link


def resource_link(name, url, logo):
    st.write(
        f"<a href='{url}'><img src='{logo}' height='50'></a>", unsafe_allow_html=True)
    st.write(f"<a href='{url}'>{name}</a>", unsafe_allow_html=True)


# Define the layout of the page
st.set_page_config(page_title="Python Resources", page_icon=":snake:")
st.title("Python Resources")
st.header("Basic Learning")

# Add the links to each resource
resource_link("SoloLearn", "https://www.sololearn.com/",
              "https://i.imgur.com/4i7c8xW.png")
resource_link("Python for Everybody", "https://www.youtube.com/watch?v=8DvywoWv6fI&list=PLRqwX-V7Uu6ZMbfy_DKQsTASlwqHnD45X",
              "https://i.imgur.com/16dU6M5.png")
resource_link("Python Crash Course", "https://www.youtube.com/watch?v=JJmcL1N2KQs&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-",
              "https://i.imgur.com/qlvPuOU.png")
resource_link("Corey Schafer Python Tutorial",
              "https://www.youtube.com/watch?v=-Rf4NfQkPfE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU", "https://i.imgur.com/gSDtBLi.png")
resource_link("Programming with Mosh Python Tutorial",
              "https://www.youtube.com/watch?v=_uQrJ0TkZlc", "https://i.imgur.com/W0UfZrA.png")
resource_link("Sentdex Python Programming Tutorial",
              "https://www.youtube.com/watch?v=oVp1vrfL_w4&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M", "https://i.imgur.com/KkZnLKJ.png")

# Add a footer with your name and contact information
st.markdown("---")
st.write("Created by Your Name")
st.write("Contact me at your.email@example.com")
