import tkinter as tk  # para criar a janela
import keyboard as kb  # para usar o ESC para fechar a janela
import random as rd  # para usar números aleatórios


# ---------------------------------------------------------------------------------------------------------------------
def escolha(x):  # recebe a escolha do jogador, marca o quadrado e desabilita
    match x:
        case 1:
            um_var.set('X')
            um_btn['state'] = tk.DISABLED
        case 2:
            dois_var.set('X')
            dois_btn['state'] = tk.DISABLED
        case 3:
            tres_var.set('X')
            tres_btn['state'] = tk.DISABLED
        case 4:
            quatro_var.set('X')
            quatro_btn['state'] = tk.DISABLED
        case 5:
            cinco_var.set('X')
            cinco_btn['state'] = tk.DISABLED
        case 6:
            seis_var.set('X')
            seis_btn['state'] = tk.DISABLED
        case 7:
            sete_var.set('X')
            sete_btn['state'] = tk.DISABLED
        case 8:
            oito_var.set('X')
            oito_btn['state'] = tk.DISABLED
        case 9:
            nove_var.set('X')
            nove_btn['state'] = tk.DISABLED

    maquina()


# ---------------------------------------------------------------------------------------------------------------------
def maquina():  # inteligencia do jogo

    if cinco_var.get() == '':  # caso o jogador não escolha o centro no início
        x = 5
    else:
        # mapea as posições que estão vazias
        posicoes_par = [2, 4, 6, 8]
        posicoes_impar = [1, 3, 5, 7, 9]

        if um_var.get() != '':
            posicoes_impar.remove(1)

        if dois_var.get() != '':
            posicoes_par.remove(2)

        if tres_var.get() != '':
            posicoes_impar.remove(3)

        if quatro_var.get() != '':
            posicoes_par.remove(4)

        if cinco_var.get() != '':
            posicoes_impar.remove(5)

        if seis_var.get() != '':
            posicoes_par.remove(6)

        if sete_var.get() != '':
            posicoes_impar.remove(7)

        if oito_var.get() != '':
            posicoes_par.remove(8)

        if nove_var.get() != '':
            posicoes_impar.remove(9)

        # começa o jogo peças pelas pontas
        if len(posicoes_impar) != 0:
            x = rd.choice(posicoes_impar)  # garante que o X não fique vazio
        else:  # quando a lista zera vai para cruz
            if len(posicoes_par) != 0:  # garante que o X não fique vazio
                x = rd.choice(posicoes_par)
            else:
                x = 0  # garante que o X não fique vazio
                placar('')  # envia para o placar o empate

    # defendendo o quadrado 1
    if quatro_var.get() == 'X' and sete_var.get() == 'X' and um_var.get() == '':
        x = 1
    if dois_var.get() == 'X' and tres_var.get() == 'X' and um_var.get() == '':
        x = 1
    if cinco_var.get() == 'X' and nove_var.get() == 'X' and um_var.get() == '':
        x = 1

    # defendendo o quadrado 2
    if um_var.get() == 'X' and tres_var.get() == 'X' and dois_var.get() == '':
        x = 2
    if cinco_var.get() == 'X' and oito_var.get() == 'X' and dois_var.get() == '':
        x = 2

    # defendendo o quadrado 3
    if um_var.get() == 'X' and dois_var.get() == 'X' and tres_var.get() == '':
        x = 3
    if seis_var.get() == 'X' and nove_var.get() == 'X' and tres_var.get() == '':
        x = 3
    if cinco_var.get() == 'X' and sete_var.get() == 'X' and tres_var.get() == '':
        x = 3

    # defendendo o quadrado 4
    if um_var.get() == 'X' and sete_var.get() == 'X' and quatro_var.get() == '':
        x = 4
    if cinco_var.get() == 'X' and seis_var.get() == 'X' and quatro_var.get() == '':
        x = 4

    # defendendo o quadrado 5
    if um_var.get() == 'X' and nove_var.get() == 'X' and cinco_var.get() == '':
        x = 5
    if tres_var.get() == 'X' and sete_var.get() == 'X' and cinco_var.get() == '':
        x = 5
    if quatro_var.get() == 'X' and seis_var.get() == 'X' and cinco_var.get() == '':
        x = 5
    if dois_var.get() == 'X' and oito_var.get() == 'X' and cinco_var.get() == '':
        x = 5

    # defendendo o quadrado 6
    if tres_var.get() == 'X' and nove_var.get() == 'X' and seis_var.get() == '':
        x = 6
    if quatro_var.get() == 'X' and cinco_var.get() == 'X' and seis_var.get() == '':
        x = 6

    # defendendo o quadrado 7
    if um_var.get() == 'X' and quatro_var.get() == 'X' and sete_var.get() == '':
        x = 7
    if tres_var.get() == 'X' and cinco_var.get() == 'X' and sete_var.get() == '':
        x = 7
    if nove_var.get() == 'X' and oito_var.get() == 'X' and sete_var.get() == '':
        x = 7

    # defendendo o quadrado 8
    if sete_var.get() == 'X' and nove_var.get() == 'X' and oito_var.get() == '':
        x = 8
    if dois_var.get() == 'X' and cinco_var.get() == 'X' and oito_var.get() == '':
        x = 8

    # defendendo o quadrado 9
    if um_var.get() == 'X' and cinco_var.get() == 'X' and nove_var.get() == '':
        x = 9
    if tres_var.get() == 'X' and seis_var.get() == 'X' and nove_var.get() == '':
        x = 9
    if sete_var.get() == 'X' and oito_var.get() == 'X' and nove_var.get() == '':
        x = 9

    # prevendo ataque duplo L
    if um_var.get() == 'X' and cinco_var.get() == 'O' and seis_var.get() == 'X':
        if tres_var.get() == '' and nove_var.get() == '':
            x = rd.choice([3, 9])
    if sete_var.get() == 'X' and cinco_var.get() == 'O' and seis_var.get() == 'X':
        if tres_var.get() == '' and nove_var.get() == '':
            x = rd.choice([3, 9])
    if um_var.get() == 'X' and cinco_var.get() == 'O' and oito_var.get() == 'X':
        if sete_var.get() == '' and nove_var.get() == '':
            x = rd.choice([7, 9])
    if tres_var.get() == 'X' and cinco_var.get() == 'O' and oito_var.get() == 'X':
        if sete_var.get() == '' and nove_var.get() == '':
            x = rd.choice([7, 9])
    if tres_var.get() == 'X' and cinco_var.get() == 'O' and quatro_var.get() == 'X':
        if um_var.get() == '' and sete_var.get() == '':
            x = rd.choice([1, 7])
    if nove_var.get() == 'X' and cinco_var.get() == 'O' and quatro_var.get() == 'X':
        if um_var.get() == '' and sete_var.get() == '':
            x = rd.choice([1, 7])
    if sete_var.get() == 'X' and cinco_var.get() == 'O' and dois_var.get() == 'X':
        if um_var.get() == '' and tres_var.get() == '':
            x = rd.choice([1, 3])
    if nove_var.get() == 'X' and cinco_var.get() == 'O' and dois_var.get() == 'X':
        if um_var.get() == '' and tres_var.get() == '':
            x = rd.choice([1, 3])

    # prevendo ataque cruzado
    if (um_var.get() == 'X' and cinco_var.get() == 'O' and nove_var.get() == 'X') or \
       (tres_var.get() == 'X' and cinco_var.get() == 'O' and sete_var.get() == 'X'):
        if dois_var.get() == '' and quatro_var.get() == '' and seis_var.get() == '' and oito_var.get() == '':
            x = rd.choice([2, 4, 6, 8])

    # prevendo ataque de canto
    if dois_var.get() == 'X' and cinco_var.get() == 'O' and quatro_var.get() == 'X':
        if um_var.get() == '' and tres_var.get() == '' and sete_var.get() == '':
            x = rd.choice([1, 3, 7])
    if quatro_var.get() == 'X' and cinco_var.get() == 'O' and oito_var.get() == 'X':
        if um_var.get() == '' and sete_var.get() == '' and nove_var.get() == '':
            x = rd.choice([1, 7, 9])
    if dois_var.get() == 'X' and cinco_var.get() == 'O' and seis_var.get() == 'X':
        if um_var.get() == '' and tres_var.get() == '' and nove_var.get() == '':
            x = rd.choice([1, 3, 9])
    if oito_var.get() == 'X' and cinco_var.get() == 'O' and seis_var.get() == 'X':
        if tres_var.get() == '' and sete_var.get() == '' and nove_var.get() == '':
            x = rd.choice([3, 7, 9])

    # ganhando no 1
    if quatro_var.get() == 'O' and sete_var.get() == 'O' and um_var.get() == '':
        x = 1
    if dois_var.get() == 'O' and tres_var.get() == 'O' and um_var.get() == '':
        x = 1
    if cinco_var.get() == 'O' and nove_var.get() == 'O' and um_var.get() == '':
        x = 1

    # ganhando no 2
    if um_var.get() == 'O' and tres_var.get() == 'O' and dois_var.get() == '':
        x = 2
    if cinco_var.get() == 'O' and oito_var.get() == 'O' and dois_var.get() == '':
        x = 2

    # ganhando no 3
    if um_var.get() == 'O' and dois_var.get() == 'O' and tres_var.get() == '':
        x = 3
    if seis_var.get() == 'O' and nove_var.get() == 'O' and tres_var.get() == '':
        x = 3
    if cinco_var.get() == 'O' and sete_var.get() == 'O' and tres_var.get() == '':
        x = 3

    # ganhando no 4
    if um_var.get() == 'O' and sete_var.get() == 'O' and quatro_var.get() == '':
        x = 4
    if cinco_var.get() == 'O' and seis_var.get() == 'O' and quatro_var.get() == '':
        x = 4

    # ganhando no 5
    if um_var.get() == 'O' and nove_var.get() == 'O' and cinco_var.get() == '':
        x = 5
    if tres_var.get() == 'O' and sete_var.get() == 'O' and cinco_var.get() == '':
        x = 5
    if quatro_var.get() == 'O' and seis_var.get() == 'O' and cinco_var.get() == '':
        x = 5
    if dois_var.get() == 'O' and oito_var.get() == 'O' and cinco_var.get() == '':
        x = 5

    # ganhando no 6
    if tres_var.get() == 'O' and nove_var.get() == 'O' and seis_var.get() == '':
        x = 6
    if quatro_var.get() == 'O' and cinco_var.get() == 'O' and seis_var.get() == '':
        x = 6

    # ganhando no 7
    if um_var.get() == 'O' and quatro_var.get() == 'O' and sete_var.get() == '':
        x = 7
    if tres_var.get() == 'O' and cinco_var.get() == 'O' and sete_var.get() == '':
        x = 7
    if nove_var.get() == 'O' and oito_var.get() == 'O' and sete_var.get() == '':
        x = 7

    # ganhando no 8
    if sete_var.get() == 'O' and nove_var.get() == 'O' and oito_var.get() == '':
        x = 8
    if dois_var.get() == 'O' and cinco_var.get() == 'O' and oito_var.get() == '':
        x = 8

    # ganhando no 9
    if um_var.get() == 'O' and cinco_var.get() == 'O' and nove_var.get() == '':
        x = 9
    if tres_var.get() == 'O' and seis_var.get() == 'O' and nove_var.get() == '':
        x = 9
    if sete_var.get() == 'O' and oito_var.get() == 'O' and nove_var.get() == '':
        x = 9

    # ações dos botões escolhidos pela máquina
    match x:
        case 1:
            um_var.set('O')
            um_btn['state'] = tk.DISABLED
        case 2:
            dois_var.set('O')
            dois_btn['state'] = tk.DISABLED
        case 3:
            tres_var.set('O')
            tres_btn['state'] = tk.DISABLED
        case 4:
            quatro_var.set('O')
            quatro_btn['state'] = tk.DISABLED
        case 5:
            cinco_var.set('O')
            cinco_btn['state'] = tk.DISABLED
        case 6:
            seis_var.set('O')
            seis_btn['state'] = tk.DISABLED
        case 7:
            sete_var.set('O')
            sete_btn['state'] = tk.DISABLED
        case 8:
            oito_var.set('O')
            oito_btn['state'] = tk.DISABLED
        case 9:
            nove_var.set('O')
            nove_btn['state'] = tk.DISABLED

    # vitórias nas colunas
    if (um_var.get() == 'X' and dois_var.get() == 'X' and tres_var.get() == 'X') or \
       (um_var.get() == 'O' and dois_var.get() == 'O' and tres_var.get() == 'O'):
        bloqueia()
        um_btn['bg'] = 'blue'  # muda a cor do botão
        dois_btn['bg'] = 'blue'
        tres_btn['bg'] = 'blue'
        placar(um_var.get())  # envia para o placar o vitorioso

    elif (quatro_var.get() == 'X' and cinco_var.get() == 'X' and seis_var.get() == 'X') or \
         (quatro_var.get() == 'O' and cinco_var.get() == 'O' and seis_var.get() == 'O'):
        bloqueia()
        quatro_btn['bg'] = 'blue'
        cinco_btn['bg'] = 'blue'
        seis_btn['bg'] = 'blue'
        placar(quatro_var.get())

    elif (sete_var.get() == 'X' and oito_var.get() == 'X' and nove_var.get() == 'X') or \
         (sete_var.get() == 'O' and oito_var.get() == 'O' and nove_var.get() == 'O'):
        bloqueia()
        sete_btn['bg'] = 'blue'
        oito_btn['bg'] = 'blue'
        nove_btn['bg'] = 'blue'
        placar(sete_var.get())

    # vitórias nas linhas
    elif (um_var.get() == 'X' and quatro_var.get() == 'X' and sete_var.get() == 'X') or \
         (um_var.get() == 'O' and quatro_var.get() == 'O' and sete_var.get() == 'O'):
        bloqueia()
        um_btn['bg'] = 'blue'
        quatro_btn['bg'] = 'blue'
        sete_btn['bg'] = 'blue'
        placar(um_var.get())

    elif (dois_var.get() == 'X' and cinco_var.get() == 'X' and oito_var.get() == 'X') or \
         (dois_var.get() == 'O' and cinco_var.get() == 'O' and oito_var.get() == 'O'):
        bloqueia()
        dois_btn['bg'] = 'blue'
        cinco_btn['bg'] = 'blue'
        oito_btn['bg'] = 'blue'
        placar(dois_var.get())

    elif (tres_var.get() == 'X' and seis_var.get() == 'X' and nove_var.get() == 'X') or \
         (tres_var.get() == 'O' and seis_var.get() == 'O' and nove_var.get() == 'O'):
        bloqueia()
        tres_btn['bg'] = 'blue'
        seis_btn['bg'] = 'blue'
        nove_btn['bg'] = 'blue'
        placar(tres_var.get())

    # vitórias nas diagonais
    elif (um_var.get() == 'X' and cinco_var.get() == 'X' and nove_var.get() == 'X') or \
         (um_var.get() == 'O' and cinco_var.get() == 'O' and nove_var.get() == 'O'):
        bloqueia()
        um_btn['bg'] = 'blue'
        cinco_btn['bg'] = 'blue'
        nove_btn['bg'] = 'blue'
        placar(um_var.get())

    elif (sete_var.get() == 'X' and cinco_var.get() == 'X' and tres_var.get() == 'X') or \
         (sete_var.get() == 'O' and cinco_var.get() == 'O' and tres_var.get() == 'O'):
        bloqueia()
        sete_btn['bg'] = 'blue'
        cinco_btn['bg'] = 'blue'
        tres_btn['bg'] = 'blue'
        placar(sete_var.get())


# ---------------------------------------------------------------------------------------------------------------------
def limpa():  # para reiniciar o jogo

    # esvazia os quadrados
    um_var.set('')
    dois_var.set('')
    tres_var.set('')
    quatro_var.set('')
    cinco_var.set('')
    seis_var.set('')
    sete_var.set('')
    oito_var.set('')
    nove_var.set('')

    # reabilita os botões
    um_btn['state'] = tk.NORMAL
    dois_btn['state'] = tk.NORMAL
    tres_btn['state'] = tk.NORMAL
    quatro_btn['state'] = tk.NORMAL
    cinco_btn['state'] = tk.NORMAL
    seis_btn['state'] = tk.NORMAL
    sete_btn['state'] = tk.NORMAL
    oito_btn['state'] = tk.NORMAL
    nove_btn['state'] = tk.NORMAL

    # pinta eles de branco
    um_btn['bg'] = 'white'
    dois_btn['bg'] = 'white'
    tres_btn['bg'] = 'white'
    quatro_btn['bg'] = 'white'
    cinco_btn['bg'] = 'white'
    seis_btn['bg'] = 'white'
    sete_btn['bg'] = 'white'
    oito_btn['bg'] = 'white'
    nove_btn['bg'] = 'white'


# ---------------------------------------------------------------------------------------------------------------------
def bloqueia():  # quando encerra o jogo
    # bloqueia todos os botões
    um_btn['state'] = tk.DISABLED
    dois_btn['state'] = tk.DISABLED
    tres_btn['state'] = tk.DISABLED
    quatro_btn['state'] = tk.DISABLED
    cinco_btn['state'] = tk.DISABLED
    seis_btn['state'] = tk.DISABLED
    sete_btn['state'] = tk.DISABLED
    oito_btn['state'] = tk.DISABLED
    nove_btn['state'] = tk.DISABLED


# ---------------------------------------------------------------------------------------------------------------------
def placar(x):

    if x == 'X':
        vitorias_var.set(str(int(vitorias_var.get())+1))  # acumula as vitórias "se ouver"
    elif x == 'O':
        derrotas_var.set(str(int(derrotas_var.get())+1))  # acumula as derrotas
    else:
        empates_var.set(str(int(empates_var.get())+1))  # acumula os empates


# ---------------------------------------------------------------------------------------------------------------------
# criação e configuração da janela
janela = tk.Tk()  # cria o objeto janela
janela.resizable(width=False, height=False)  # desativa a mudança de tamanho
janela.title('#')
# tamanho: 325X250, posição: calula e posiciona
janela.geometry("%dx%d%d%d" % (190, 290, float(190 / 2 - janela.winfo_screenwidth() / 2),
                               float(290 / 2 - janela.winfo_screenheight() / 2)))
# ---------------------------------------------------------------------------------------------------------------------
url_texto = tk.Label(janela, text='Jogo da velha', font=('', 12))  # título da janela
url_texto.place(x=10, y=10)  # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
con_txt_btn = tk.Button(janela, text='Limpar', command=lambda: limpa())  # criando objeto botão
con_txt_btn.place(x=130, y=10, width=50)  # posicionando botão
# ---------------------------------------------------------------------------------------------------------------------
um_var = tk.StringVar()  # objeto string usado para o tkinter
um_var.set('')  # definindo ela como vazia
um_btn = tk.Button(janela, textvariable=um_var, command=lambda: escolha(1), font=('', 30))  # criando objeto botão
um_btn.place(x=10, y=40, width=50, height=50)  # posicionando botão
um_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
dois_var = tk.StringVar()
dois_var.set('')
dois_btn = tk.Button(janela, textvariable=dois_var, command=lambda: escolha(2), font=('', 30))
dois_btn.place(x=10, y=100, width=50, height=50)
dois_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
tres_var = tk.StringVar()
tres_var.set('')
tres_btn = tk.Button(janela, textvariable=tres_var, command=lambda: escolha(3), font=('', 30))
tres_btn.place(x=10, y=160, width=50, height=50)
tres_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
quatro_var = tk.StringVar()
quatro_var.set('')
quatro_btn = tk.Button(janela, textvariable=quatro_var, command=lambda: escolha(4), font=('', 30))
quatro_btn.place(x=70, y=40, width=50, height=50)
quatro_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
cinco_var = tk.StringVar()
cinco_var.set('')
cinco_btn = tk.Button(janela, textvariable=cinco_var, command=lambda: escolha(5), font=('', 30))
cinco_btn.place(x=70, y=100, width=50, height=50)
cinco_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
seis_var = tk.StringVar()
seis_var.set('')
seis_btn = tk.Button(janela, textvariable=seis_var, command=lambda: escolha(6), font=('', 30))
seis_btn.place(x=70, y=160, width=50, height=50)
seis_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
sete_var = tk.StringVar()
sete_var.set('')
sete_btn = tk.Button(janela, textvariable=sete_var, command=lambda: escolha(7), font=('', 30))
sete_btn.place(x=130, y=40, width=50, height=50)
sete_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
oito_var = tk.StringVar()
oito_var.set('')
oito_btn = tk.Button(janela, textvariable=oito_var, command=lambda: escolha(8), font=('', 30))
oito_btn.place(x=130, y=100, width=50, height=50)
oito_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
nove_var = tk.StringVar()
nove_var.set('')
nove_btn = tk.Button(janela, textvariable=nove_var, command=lambda: escolha(9), font=('', 30))
nove_btn.place(x=130, y=160, width=50, height=50)
nove_btn['bg'] = 'white'
# ---------------------------------------------------------------------------------------------------------------------
vi_txt = tk.Label(janela, text='Votórias:')  # criando objeto de texto simples
vi_txt.place(x=10, y=220)
# ---------------------------------------------------------------------------------------------------------------------
de_txt = tk.Label(janela, text='Derrotas:')
de_txt.place(x=10, y=240)
# ---------------------------------------------------------------------------------------------------------------------
em_txt = tk.Label(janela, text='Empates:')
em_txt.place(x=10, y=260)
# ---------------------------------------------------------------------------------------------------------------------
vitorias_var = tk.StringVar()  # objeto string usado para o tkinter
vitorias_var.set('0')  # começa com o valor zerado
vitorias_txt = tk.Label(janela, textvariable=vitorias_var)  # criando objeto de texto
vitorias_txt.place(x=60, y=220)
# ---------------------------------------------------------------------------------------------------------------------
derrotas_var = tk.StringVar()
derrotas_var.set('0')
derrotas_txt = tk.Label(janela, textvariable=derrotas_var)
derrotas_txt.place(x=60, y=240)
# ---------------------------------------------------------------------------------------------------------------------
empates_var = tk.StringVar()
empates_var.set('0')
empates_txt = tk.Label(janela, textvariable=empates_var)
empates_txt.place(x=60, y=260)
# ---------------------------------------------------------------------------------------------------------------------
em_txt = tk.Label(janela, text='#', font=('', 40))  # hashtag no canto da tela
em_txt.place(x=140, y=220)
# ---------------------------------------------------------------------------------------------------------------------
kb.on_press_key('ENTER', lambda _: limpa())  # comando para recomeçar
kb.on_press_key('ESC', lambda _: janela.destroy())  # comando para fechar a janela
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()  # mantem a janela aberta
