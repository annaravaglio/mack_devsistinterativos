from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkMessageBox
from tkinter import messagebox, Canvas, Frame, BOTH
from random import randint
from PIL import Image, ImageTk
import cv2
from datetime import time, date, datetime

#estrutura
#https://github.com/ripexz/python-tkinter-minesweeper

varDificuldade = 0
varCorClick = "#000000"
varCorNoClick = "#FFFFFF"
varQtdBolinhas = 100
varCores = 0
varTentativas = 5
tamanho_X = 10
tamanho_Y = 10
noClick = 0
click = 1
buttom_click = "<Button-1>"

class clickColor:

    def __init__(self, tk):

        self.images = {
            "bolinhaNoClick": PhotoImage(file = "C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\bolinhaNoClick.png"),
            "bolinhaClick": PhotoImage(file = "C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\bolinhaClick.png")
        }

        # set up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # set up labels/UI
        self.labels = {
            "Tempo": Label(self.frame, text = "00:00:00",font=("Calibri", 25)),
            "Tentativas": Label(self.frame, text = "Tentativas: 1 de 5",font=("Calibri", 25)),
            "Acertos": Label(self.frame, text = "Acertos: 0 ",font=("Calibri", 25)),
            "Total": Label(self.frame, text = "Total: 100",font=("Calibri", 25))
        }
        self.labels["Tempo"].grid(row = 0, column = 0, columnspan = tamanho_Y) # top full width
        self.labels["Tentativas"].grid(row = tamanho_X+1, column = 0, columnspan = int(tamanho_Y/2)) # bottom left
        self.labels["Acertos"].grid(row = tamanho_X+1, column = int(tamanho_Y/2)-1, columnspan = int(tamanho_Y/2)) # bottom right
        self.labels["Total"].grid(row = tamanho_Y+1, column = int(tamanho_X/2)-1, columnspan = int(tamanho_X/2)) # bottom right

        self.restart() # start game
        self.updateTimer() # init timer

    def setup(self):
        # create flag and clicked tile variables
        self.acertos = 0
        self.total = 0
        self.tentativas = 0
        self.startTime = None

        # create buttons
        self.tiles = dict({})
        self.mines = 0
        for x in range(0, tamanho_X):
            for y in range(0, tamanho_Y):
                if y == 0:
                    self.tiles[x] = {}

                id = str(x) + "_" + str(y)
                isMine = False

                # tile image changeable for debug reasons:
                gfx = self.images["bolinhaNoClick"]

                # currently random amount of mines
                tile = {
                    "id": id,
                    "state": noClick,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "button": Button(self.frame, image = gfx)
                }

                tile["button"].bind(buttom_click, self.onClickWrapper(x, y))
                tile["button"].grid( row = x+1, column = y ) # offset by 1 row for timer

                self.tiles[x][y] = tile

    def restart(self):
        self.setup()
        self.refreshLabels()

    def refreshLabels(self):
        self.labels["Tentativas"].config(text = "Tentativas: "+str(self.tentativas))
        self.labels["Acertos"].config(text = "Acertos: "+str(self.acertos))
        self.labels["Total"].config(text = "Total: "+str(self.total))

    def gameOver(self, won):

        self.tk.update()

        msg = "You Win! Play again?" if won else "You Lose! Play again?"
        res = tkMessageBox.askyesno("Game Over", msg)
        if res:
            self.restart()
        else:
            self.tk.quit()

    def updateTimer(self):
        ts = "00:00:00"
        if self.startTime != None:
            delta = datetime.now() - self.startTime
            ts = str(delta).split('.')[0] # drop ms
            if delta.total_seconds() < 36000:
                ts = "0" + ts # zero-pad
        self.labels["Tempo"].config(text = ts)
        self.frame.after(100, self.updateTimer)

    def onClickWrapper(self, x, y):
        return lambda Button: self.onClick(self.tiles[x][y])

    def onClick(self, tile):
        if self.startTime == None:
            self.startTime = datetime.now()

        if tile["state"] != click:
            tile["button"].config(image = self.images["bolinhaClick"])
            tile["state"] = click
            self.acertos += 1

def rankingExport():
    print("hello")
def rankingVisualiza():
    print("hello")
def rankingLimpa():
    print("hello")
def novoJogo():
    print("hello")
def iniciarJogo():
    print("hello")
def marcarBolinha():
    print("hello")
def selecionarDificuldade():
    win = Toplevel() #Subjanela
    win.title("Dificuldade")
    win.geometry("300x100")

def configuracao():
    print("hello")

janela = Tk()
janela.title("Projeto - colorReact")
janela.geometry("1024x700")
janela.resizable(False, False)

meu_menu = Menu(janela)
janela.config(menu=meu_menu)

menu_novoJogo = Menu(meu_menu, tearoff=0).add_command(novoJogo())
menu_dificuldade = Menu(meu_menu, tearoff=0)
menu_ranking = Menu(meu_menu, tearoff=0)
menu_ranking.add_command(label="Planilha", command=rankingExport)
menu_ranking.add_command(label="Visualizar", command=rankingVisualiza)
menu_ranking.add_separator()
menu_ranking.add_command(label="Apagar", command=rankingLimpa)
menu_configuracao = Menu(meu_menu, tearoff=0)

meu_menu.add_cascade(label="Novo Jogo", menu=menu_novoJogo, command=novoJogo)
meu_menu.add_cascade(label="Dificuldade", menu=menu_dificuldade, command=selecionarDificuldade)
meu_menu.add_cascade(label="Ranking", menu=menu_ranking)
meu_menu.add_cascade(label="Configuração", menu=menu_dificuldade, command=configuracao)

nuvem = PhotoImage(file="C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\nuvem.png")
nuvem2 = PhotoImage(file="C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\nuvem2.png")
bolinhaClick = PhotoImage(file="C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\bolinhaClick.png")
bolinhaNoClick = PhotoImage(file="C:\\Users\\annar\\OneDrive\\Documentos\\Github\\mack_devsistinterativos\\Projeto\\img\\bolinhaNoClick.png")

logo = Label(janela, justify=LEFT, compound = CENTER, padx = 5, image=nuvem, font=("Calibri", 25)).pack(side="left",anchor=NW)
# iniciar = Button(janela, text="Iniciar", font=("Calibri", 25), command=iniciarJogo).pack(side="top",anchor=N)
dificuldade = Label(janela, justify=LEFT, compound = CENTER, padx = 5, text="Dificuldade", image=nuvem2, font=("Calibri", 25), textvariable=varDificuldade).pack(side="right",anchor=NE)
telaBolinhas = Frame()
colorReact = clickColor(telaBolinhas)
telaBolinhas.pack(side="top",anchor=E)


janela.mainloop()