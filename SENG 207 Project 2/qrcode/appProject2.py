import PySimpleGUI as sg
import qrcode
import os

sg.theme('Dark')
layout = [
    [sg.Input(key='-WEB-ADDRESS-')],
    [sg.Button('Generate QR Code', key='-GENERATE_QR_CODE-')],
    [sg.Image(key='-IMAGE-', size=(300, 300))]
]

window = sg.Window('QR Code Generator', layout)


def generate_qr_code(link):
   
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = "qr_code"+ ".png"
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-GENERATE_QR_CODE-':
        web_address = values['-WEB-ADDRESS-']
        qr_code_image_path = generate_qr_code(web_address)
        window['-IMAGE-'].update(filename=qr_code_image_path)

window.close()
