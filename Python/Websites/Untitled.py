# Import the required libraries
import streamlit as st

# Define the main function that runs the website


def main():
    # Set the title of the website
    st.set_page_config(
        page_title="Python Learning Resources",
        page_icon=":snake:"
    )

    # Define the logo
    logo = "https://logodownload.org/wp-content/uploads/2019/10/python-logo-3.png"

    # Add the logo and title to the website
    st.image(logo, width=400)
    st.title("Python Learning Resources")

    # Define the Homepage sub-page
    if st.sidebar.button("Homepage", key='home_button'):
        st.image(logo, width=400)
        st.title("Python Learning Resources")
        st.write("# Homepage")
        st.write("Welcome to the Python Learning Resources website! Here you will find a curated list of resources to help you learn Python. Use the navigation bar on the left to explore the different sections of the website.")

    # Define the Navigation section
    st.sidebar.title("Navigation")

    # Define the SoloLearn sub-page
    if st.sidebar.button("SoloLearn"):
        st.image(logo, width=400)
        st.title("Python Learning Resources")
        st.write("# SoloLearn")

    # Define the Python Resources sub-page
    if st.sidebar.button("Python Resources"):
        st.image(logo, width=400)
        st.title("Python Learning Resources")
        st.write("# Python Resources")

    # Define the Python Video Tutorials sub-page
    if st.sidebar.button("Python Video Tutorials"):
        st.image(logo, width=400)
        st.title("Python Learning Resources")
        st.write("# Python Video Tutorials")

    # Define the Python Projects sub-page
    if st.sidebar.button("Python Projects"):
        st.image(logo, width=400)
        st.title("Python Learning Resources")
        st.write("# Python Projects")


# Call the main function to run the website
if __name__ == "__main__":
    main()
