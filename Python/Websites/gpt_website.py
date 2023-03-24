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

    # Define the description section
    st.write("Welcome to the Python Learning Resources website! Here you will find a curated list of resources to help you learn Python. Use the navigation bar on the left to explore the different sections of the website.")
    st.write("To get started, we recommend checking out the SoloLearn section for free coding courses or the Python Resources section for tutorials and articles on Python programming.")

    # Define the Navigation section
    st.sidebar.title("Navigation")

    # add a button to the sidebar to return to the homepage
    if st.sidebar.button("Home", key='home_button'):
        st.experimental_rerun()

    # Define the SoloLearn sub-page
    if st.sidebar.button("SoloLearn"):
        st.write("# SoloLearn")
        st.write("SoloLearn is a mobile and web-based platform that offers free coding courses in various programming languages, including Python.")
        st.write("Click the link below to visit the SoloLearn website:")
        st.write("- [SoloLearn](https://www.sololearn.com/)")

    # Define the Python Resources sub-page
    if st.sidebar.button("Python Resources"):
        st.write("# Python Resources")
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

    # Define the Python Video Tutorials sub-page
    if st.sidebar.button("Python Video Tutorials"):
        st.write("# Python Video Tutorials")
        st.write("Here are some short video tutorials to help you learn Python:")
        st.write(
            "- [Python in 100 Seconds](https://youtu.be/x7X9w_GIm1s)")
        st.write(
            "- [Python Crash Course](https://youtu.be/JJmcL1N2KQs)")
        st.write(
            "- [Python Functions](https://youtu.be/9Os0o3wzS_I)")
        st.write(
            "- [Python Full Course - Programming with Mosh](https://youtu.be/_uQrJ0TkZlc)")
        st.write(
            "- [Python Full Course - freeCodeCamp](https://youtu.be/rfscVS0vtbw)")

    # Define the Python Projects sub-page
    if st.sidebar.button("Python Projects"):
        st.write("# Python Projects")
        st.write(
            'Building hands-on projects will help you gain practical coding skills. One step at a time, you\'ll be putting your theoretical knowledge to use and build an impressive portfolio. If you are an experienced Python Developer, You might have heard as well as searched for this question "What are some python projects for beginners & those at an intermediate skill-level and which projects should I work on to gain real time experience?" (when you\'re a beginner) in different communities like GitHub, Reddit or Quora.')
        st.write('So, to help you with that, here is a list of 70+ simple python projects for beginners, Intermediate and advanced python programmers with source code. This projects will be suitable for python programmers, machine learning with python practitioners, data science with python enthusiasts, etc.')
        st.write('These python projects are a great way to learn python and build your portfolio. You can use these python projects as a reference to build your own projects.')
        st.header("Website")
        st.write(
            "[70+ Simple And Advanced Python Porjects With Source Code](https://www.theinsaneapp.com/2021/06/list-of-python-projects-with-source-code-and-tutorials.html)")


# Call the main function to run the website
if __name__ == "__main__":
    main()
