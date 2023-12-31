# age = int(input("Enter your age : "))


# if age > 100:
#     print("You are dead!")
# elif age > 65:
#     print("Enjoy your retirement!")
# elif age > 40:
#     print("You are over the hill!")
# elif age < 13:
#     print("You qualify for the kiddie discount!")
# elif age == 21:
#     print("Congrats on your 21st!")
# else:
#     print("Age is but a number!")


import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()