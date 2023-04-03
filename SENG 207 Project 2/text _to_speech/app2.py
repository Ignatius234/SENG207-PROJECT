import PySimpleGUI as sg
import pyttsx3

speaker = pyttsx3.init()

layout = [
    [sg.Text('Enter your text:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Text('Select a voice:')],
    [sg.Radio('Male', "RADIO1", default=True, key='-MALE-'),
     sg.Radio('Female', "RADIO1", key='-FEMALE-'),
     ],
    [sg.Text('VOLUME: '),
     sg.Slider(key='-VOLUME-',range=(0,10), size=(18, 15), orientation='horizontal')],
    [sg.Button('Speak'), sg.Button('Exit')]
]

window = sg.Window('TEXT TO SPEECH APP', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # Launch the pyttsx3 engine.
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')
        set_volume = values['-VOLUME-']
        # Access the text in the input box.
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        # pick the voice type.
        if values['-MALE-']:
            engine.setProperty('voice', voices[0].id)
        elif values['-FEMALE-']:
            engine.setProperty('voice', voices[1].id)
           
        engine.setProperty('volume', set_volume )
        engine.say(text)

        engine.runAndWait()


window.close()
