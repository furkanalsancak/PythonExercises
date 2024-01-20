from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Create the main window
window = Tk()
window.geometry("800x500")
window.resizable(0,0) #disabling the GUI size to get bigger or smaller. A fit size
window.title("GUI")
window.configure(bg="white")

image = Image.open('C:\\Users\\furka\\Desktop\\download.png')
image = ImageTk.PhotoImage(image)

image_label = Label(window, image=image)
image_label.pack()

#Create a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

#Create a file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

#Add menu items to the file menu
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

#Create an edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

#Add menu items to the edit menu
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

#Create a help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

#Add menu items to the Help menu
help_menu.add_command(label="About GUI")




#Create a label
label_1 = Label(text="Click the button",  bg="green", width="800", height="2", font=("Arial Bold", 15))
label_1.pack()


def show_message():
   message_box = messagebox.showinfo("Message", "Hello")

#function to change label text once an action happens
def on_button_click():
    if label_1.cget("text") == "Click the button" or label_1.cget("text") == "Button Unclicked!":
        label_1.config(text="Button Clicked!")
    else:
        label_1.config(text="Button Unclicked!")

button_1 = Button(window, text="Show Message",bg="Purple",fg="white", height="2", width="20", font=("Arial",15), command=show_message)
button_1.pack()

Label(text="", bg="white").pack()

#create a button
button_2 = Button(text="Click me", bg="Purple",fg="white", height="2", width="20", font=("Arial",15), command=on_button_click )
button_2.pack() 

#start the event loop
window.mainloop()
