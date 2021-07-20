import random
import PySimpleGUI as sg


class GeraSenha:
    def __init__(self):
        sg.theme('Python')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]
        ]

        self.janela = sg.Window('Gerador de senhas', layout)

    def iniciar(self):
        while True:
            acao, conteudo = self.janela.read()
            if acao == sg.WINDOW_CLOSED:
                break
            if acao == 'Gerar senha':
                nova_senha = self.gerar_senha(conteudo)
                print(nova_senha)
                self.salvar_senha(nova_senha, conteudo)

    def gerar_senha(self, valores):
        lista_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*'
        chars = random.choices(lista_char, k=int(valores['total_chars']))
        senha = ''.join(chars)
        return senha

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='', encoding='utf-8') as arq:
            arq.write(f"Site/Software: {valores['site']}, Usuário: {valores['usuario']}, Nova senha: {nova_senha}\n")

        print('\nArquivo salvo!')    


gen = GeraSenha()
gen.iniciar()