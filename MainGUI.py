import PySimpleGUI as sg
from ScreenShot import screenShot
from AutoRegister import register
from Timer import countdown_timer
from testing import testingAutoPyGui

text = ("This app is to test creating facebook account automatically, and \nperforming other tasks like fake "
        "commenting and"
        "liking\nPlease note that must click on step 1 onward")

buttonSC = sg.Button("Must screen shot the screen first (click here before starting)",
                     auto_size_button=True, mouseover_colors="Green")
buttonRegister = sg.Button("Auto register new account (1 time per account)",
                           auto_size_button=True, visible=True, mouseover_colors="Green")
buttonLike = sg.Button("Auto like (maybe in input in process not yet)",
                       auto_size_button=True, visible=True, mouseover_colors="Green")
buttonComment = sg.Button("Auto comment (maybe in input in process not yet)",
                          auto_size_button=True, visible=True, mouseover_colors="Green")

layout = [[sg.Text(text)],
          # make the button in correct size
          [buttonSC],
          [buttonRegister],
          [buttonLike],
          [buttonComment],
          [sg.Button("Exit", auto_size_button=True, mouseover_colors="Red")]
          ]

# Create the Window
window = sg.Window('App To Automate', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # run each function here
    if event == 'Must screen shot the screen first (click here before starting)':
        duration = 2  # todo: duration to control the flow of starting point.
        countdown_timer(duration)
        screenShot()

    if event == 'Auto register new account (1 time per account)':
        print(event)

    if event == 'Auto like (maybe in input in process not yet)':
        print(event)

    if event == 'Auto comment (maybe in input in process not yet)':
        print(event)

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # print('Hello', values[0], '!')

window.close()
