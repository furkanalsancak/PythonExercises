from tkinter import *

#First attempt at creating GUI using Tkinter - a built in Python module used for creating GUIs

# Function for window
def windowScreen():

    # Creating GUI page
    window = Tk()
    window.geometry("800x500")
    window.title("User Interface")

    #Adding labels to the GUI
    Label(text="Version 1.2.1", bg="green", width="800", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="").pack()

    #Adding buttons to the GUI
    Button(text="Create Account", bg="Purple", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Login", bg="yellow", height="2", width="30").pack()
    
    #Starting the event loop
    window.mainloop()


# Calling function
windowScreen()