"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2021-04-23
"""

import PySimpleGUI as sg


layout = [[sg.Text('Running')], [sg.Button('Exit')]]
# Create window
window = sg.Window('Borrow My Tools', layout)

# Create event loop
while True:
    event, values = window.read()
    # End program if user closes window or presses "Exit"
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

window.close()
