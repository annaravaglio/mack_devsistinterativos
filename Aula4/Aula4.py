import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

janela = tk.Tk()
janela.title("Jogo da Velha - Anna Ravaglio")

#Criando os frames
framePlacar = tk.Frame(janela, width=400, height=100)
frameGame = tk.Frame(janela, bg='yellow', width=400, height=250)
frameInfo = tk.Frame(janela, bg='black', width=400, height=100)
framePlacar.pack()
frameGame.pack()
frameInfo.pack()

rodadaJogador = tk.StringVar(janela, 'X')
marcarOpcao = tk.StringVar()
charGame1 = tk.StringVar()
charGame2 = tk.StringVar()
charGame3 = tk.StringVar()
charGame4 = tk.StringVar()
charGame5 = tk.StringVar()
charGame6 = tk.StringVar()
charGame7 = tk.StringVar()
charGame8 = tk.StringVar()
charGame9 = tk.StringVar()

def MarcarOpcao(button_press):
    if button_press == 1:
        if charGame1.get() == 1:
            if rodadaJogador.get() == 'X':
                bt1.config(fg='red')
                charGame1.set('X')
            else:
                bt1.config(fg='blue')
                charGame1.set('O')

def verificaVencedor():
    lb = tk.Label('Configurar a verificação do vencedor para próxima aula')

#Montando o Placar
pointsPX = tk.IntVar()
pointsPO = tk.IntVar()
pointsPX.set(0)
pointsPO.set(0)

labelPX = tk.Label(framePlacar, text='PX', font=('Helvetica', 32), fg='red')
placarPX = tk.Label(framePlacar, font=('Terminal', 32), width=2, fg='yellow', bg='black', textvariable=pointsPX, justify='center')
labelVS = tk.Label(framePlacar, text='x', font=('Helvetica', 32), fg='black', width=6)
labelPO = tk.Label(framePlacar, text='PX', font=('Helvetica', 32), fg='blue')
placarPO = tk.Label(framePlacar, font=('Terminal', 32), width=2, fg='yellow', bg='black', textvariable=pointsPX, justify='center')

labelPX.grid(row=0, column=0, sticky=tk.W)
placarPX.grid(row=0, column=1, sticky=tk.W)
labelVS.grid(row=0, column=2, sticky=tk.W)
labelPO.grid(row=0, column=3, sticky=tk.W)
placarPO.grid(row=0, column=4, sticky=tk.W)

#Montando o frameJogo

bt1 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=1: MarcarOpcao(m), textvariable=charGame1)
bt2 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=2: MarcarOpcao(m), textvariable=charGame2)
bt3 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=3: MarcarOpcao(m), textvariable=charGame3)
bt4 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=4: MarcarOpcao(m), textvariable=charGame4)
bt5 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=5: MarcarOpcao(m), textvariable=charGame5)
bt6 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=6: MarcarOpcao(m), textvariable=charGame6)
bt7 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=7: MarcarOpcao(m), textvariable=charGame7)
bt8 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=8: MarcarOpcao(m), textvariable=charGame8)
bt9 = tk.Button(frameGame, font=('Helvetica', 32), text= ' ', width=6, justify='center', relief='groove', height='2', command=lambda m=9: MarcarOpcao(m), textvariable=charGame9)

bt1.grid(row=0, column=0, sticky=tk.W)
bt2.grid(row=0, column=1, sticky=tk.W)
bt3.grid(row=0, column=2, sticky=tk.W)
bt4.grid(row=1, column=0, sticky=tk.W)
bt5.grid(row=1, column=1, sticky=tk.W)
bt6.grid(row=1, column=2, sticky=tk.W)
bt7.grid(row=2, column=0, sticky=tk.W)
bt8.grid(row=2, column=1, sticky=tk.W)
bt9.grid(row=2, column=2, sticky=tk.W)

#Montando o Footer - Vez X ou O
varInfo = tk.StringVar()
varInfo.set('Rodada do Jogador X')

labelInfo = tk.Label(frameInfo, font=('Terminal', 12), bg='black', fg='yellow', width='38', pady='4', textvariable=varInfo, justify='center')
labelInfo.pack(fill=tk.X, expand=True)

janela.mainloop()