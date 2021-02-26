import PySimpleGUI as sg
sg.theme('DarkAmber')
layout = [[sg.Text("Hello! Welcome to the GroceryChecker")], [sg.Button("Begin"), sg.Button("END")]]

window = sg.Window("Introduction",layout)
textin =''
def popup(textout):
    sg.popup(textout)
    
def secondpage():
    global textin
    layout = [[sg.Text("Search page")],
               [sg.Text("Enter your product selection below :"), sg.InputText(key='-IN-',size=(20,1))],
                [sg.Button('Read'),sg.Button('END')]]
    window = sg.Window('', layout, modal=True)
    while True:
        event, values = window.read()
        try:
            if event == "Read":
                textin = values['-IN-']
                break
        except:
            textin = ""
        if event in (sg.WIN_CLOSED, 'END'):
            break
        elif textin != "":
            textin = values['-IN-']
        else:
            pass
    window.close()
    
def Mainpage():
    while True:
        event, values = window.read()

        if event == "Begin":
            window.close()
            secondpage()
            break
        elif event in (sg.WIN_CLOSED, 'END'):
            break
    window.close()
Mainpage()

    


