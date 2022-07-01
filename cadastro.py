from  PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkPurple4')

layout = [
    [sg.Text('Usuario:', size = (8,1)), sg.Input(key='usuario', size = (20,1))],
    [sg.Text('Senha:', size = (8,1)), sg.Input(key='senha', size = (20,1),password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')],
    [sg.Output(size=(28, 5))]
]

# Janela

janela = sg.Window('Tela de Login', layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Victor Pascon' and valores['senha'] == '310721':
            print('Sejá muito bem-vindo, Victor!')
        elif valores['usuario'] == 'Marilaine' and valores['senha'] == '310721':
            print('Seja bem-vindo, Marilaine!')
        elif valores['usuario'] == 'Doctor Dani' and valores['senha'] == '137':
            print('Seja muito bem-vindo, Doctor Dani!')
        elif valores['usuario'] == 'Juba' and valores['senha'] == '1108':
            print('Seja muito bem-vinda, Juba!')
        else:
            print('Usuario não Cadastrado')
