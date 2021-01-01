import PySimpleGUI as sg

encrypt_text = [
    [sg.Image(r'C:\Users\user1\Desktop\MyScripts\PythonScripts\gui\Julius_Caesar.png',
                  background_color='black')],
        [sg.Text('Input text what encrypt', 
                  background_color='yellow', text_color='black')],
        [sg.Input(size=(19, 1), key='-INPUT-',
                  background_color='black', text_color='yellow')],
        [sg.Text('encrypt text: ', size=(19, 6), key='-OUTPUT-',
                  background_color='black', text_color='yellow')],
        [sg.Button('translate', button_color=('black', 'yellow'))]
    ]

decrypt_text = [
    [sg.Image(r'C:\Users\user1\Desktop\MyScripts\PythonScripts\gui\Julius_Caesar2.png',
              background_color='black')],
    [sg.Text('Input text what decrypt',
              background_color='yellow', text_color='black')],
    [sg.Input(size=(19, 1), key='-INPUT2-',
              background_color='black', text_color='yellow')],
    [sg.Text('decrypt text: ', size=(19, 6), key='-OUTPUT2-',
              background_color='black', text_color='yellow')],
    [sg.Button('translate', button_color=('black', 'yellow'))]
]

#bye = [sg.Button('bye', button_color=('black', 'yellow'))]

layout = [
    [sg.Column(encrypt_text, background_color='black'),
    sg.VSeperator(),
    sg.Column(decrypt_text, background_color='black')]
    #sg.VSeperator(),
    #sg.Column(bye, background_color='black')]
]

def encrypt_caesar(plaintext):
    ciphertext = []
    for s in (plaintext):
        symb_code = ord(s)
        symb_code += 3
        ciphertext.append(chr(symb_code))

    window['-OUTPUT-'].update('encrypt text: ' +
                              ''.join(ciphertext), text_color='yellow')


def decrypt_caesar(ciphertext):
    decrypttext = []
    for s in ciphertext:
      symb_code = ord(s)
      symb_code -= 3
      decrypttext.append(chr(symb_code))

    window['-OUTPUT2-'].update('decrypt text: ' +
                               ''.join(decrypttext), text_color='yellow')

#sg.theme('black')
window = sg.Window('Gaius Julius Caesar,'
                   ' immortal Dictator of the Roman Republic', 
                   layout=layout, background_color='black',
                   size=(450, 450))


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'bye':
        break
    try:
        encrypt_caesar(values['-INPUT-'])
        decrypt_caesar(values['-INPUT2-'])
    except TypeError:
        continue

if __name__=='__main__':  
    window.close()
