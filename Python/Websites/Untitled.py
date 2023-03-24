# Import the required libraries
import streamlit as st
from streamlit import caching

# Define the main function that runs the website


def main():
    # Use SessionState to keep track of whether the user has already visited the homepage
    session_state = st.session_state.get(
        "visited_homepage", {"visited": False})
    if not session_state["visited"]:
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

        # Set the session state to mark the homepage as visited
        session_state["visited"] = True
    else:
        # Add a button to allow the user to return to the homepage
        if st.button("Return to Homepage"):
            caching.clear_cache()

    # Define the Navigation section
    st.sidebar.title("Navigation")

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
            "Here are some Python Projects to help you practice your Python skills:")
        st.header("Web Scraper")
        st.write(
            "Build a Python program that can scrape data from the web and store it in a file or database.")
        st.write("[Real Python: Building a Web Scraper with Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/)")

        st.header("Chatbot")
        st.write("Create a chatbot using Python and machine learning algorithms that can chat with users and respond to their queries.")
        st.write(
            "[Real Python: How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)")

        st.header("Desktop Application")
        st.write(
            "Build a desktop application using Python and GUI frameworks like Tkinter, PyQT, or WxPython.")
        st.write(
            "[Real Python: Building a GUI Application with Tkinter](https://realpython.com/python-gui-tkinter/)")

        st.header("Image Processing")
        st.write("Develop a Python program that can manipulate images by applying filters, cropping, resizing, and other operations.")
        st.write(
            "[Real Python: Image Processing in Python with Pillow](https://realpython.com/pillow-python-image-processing/)")

        st.header("Data Analysis")
        st.write(
            "Use Python libraries like Pandas and Numpy to analyze and visualize data sets.")
        st.write(
            "[Real Python: Pandas DataFrame: The Ultimate Guide](https://realpython.com/pandas-dataframe/)")

        st.header("IoT Projects")
        st.write(
            "Build IoT projects using Raspberry Pi or Arduino boards and Python programming.")
        st.write("[Real Python: Getting Started with Raspberry Pi GPIO Pins](https://realpython.com/getting-started-with-raspberry-pi-gpio/)")

        st.header("Game Development")
        st.write(
            "Create simple games like tic-tac-toe, hangman, or snake using Python and Pygame.")
        st.write(
            "[Real Python: Introduction to Pygame: Build a Space Invaders Clone](https://realpython.com/pygame-a-primer/)")

        st.header("Automation")
        st.write("Develop automation scripts using Python to automate repetitive tasks like data entry, file manipulation, and more.")
        st.write("[Real Python: Python Automation: Robust, Repeatable, and Readable](https://realpython.com/python-automation-robust-repeatable-readable/)")

        st.header("Machine Learning")
        st.write(
            "Build a machine learning model using Python and popular libraries like Scikit-learn or TensorFlow.")
        st.write("[Real Python: Introduction to Machine Learning with Python and Scikit-Learn](https://realpython.com/learning-paths/machine-learning-python-scikit-learn/)")

        st.header("Web Development")
        st.write(
            "Create web applications using Python web frameworks like Flask, Django, or Pyramid.")
        st.write("[Real Python: Flask by Example – Setting Up a Python Project](https://realpython.com/flask-by-example-series-setting-up-a-production-ready-web-app/)")

        # add a button to the sidebar to return to the homepage
    if st.sidebar.button("Homepage", key='home_button'):
        st.experimental_rerun()


# Call the main function to run the website
if __name__ == "__main__":
    main()
