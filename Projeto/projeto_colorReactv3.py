from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkMessageBox
from tkinter import messagebox, Canvas, Frame, BOTH
from random import randint
from PIL import Image, ImageTk
import cv2
from datetime import time, date, datetime
import os
import csv

#estrutura
#https://github.com/ripexz/python-tkinter-minesweeper

varDificuldade = 0
varCorClick = "#000000"
varCorNoClick = "#FFFFFF"
varCores = 0
varTempo = 5
varTentativas = 5
tamanho_X = 10 #Linha
tamanho_Y = 9 #Coluna
varQtdBolinhas = tamanho_X * tamanho_Y
bolinhaNoClick = 0
bolinhaClick = 1
x = 0
y = 0

buttom_click = "<Button-1>"

diretorio = os.path.dirname(__file__)

class clickColor:

    def __init__(self, tk):

        self.images = {
            "bolinhaNoClick": PhotoImage(file = os.path.join(diretorio , 'img\\bolinhaNoClick.png')),
            "bolinhaClick": PhotoImage(file = os.path.join(diretorio , 'img\\bolinhaClick.png'))
        }

        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        self.labels = {
            "Tempo": Label(self.frame, text = "00:00:00",font=("Calibri", 25)),
            "Tentativas": Label(self.frame, text = "Tentativas: 1 de 5",font=("Calibri", 25)),
            "Acertos": Label(self.frame, text = "Acertos: 0 ",font=("Calibri", 25)),
            "Total": Label(self.frame, text = "Total: 100",font=("Calibri", 25))
        }
        self.labels["Tempo"].grid(row = 0, column = 0, columnspan = tamanho_Y)
        self.labels["Tentativas"].grid(row = tamanho_X+1, column = 0, columnspan = int(tamanho_X/2), rowspan=2)
        self.labels["Acertos"].grid(row = tamanho_X+1, column = int(tamanho_Y/2)+2, columnspan = int(tamanho_X/2))
        self.labels["Total"].grid(row = tamanho_X+2, column = int(tamanho_X/2), columnspan = int(tamanho_X/2))

        self.iniciar()
        self.atualizar()

    def iniciar(self):

        self.acertos = 0
        self.total = varQtdBolinhas
        self.tentativas = 0
        self.inicioTempo = None
        
        self.quadrado = dict({})

        for x in range(0, tamanho_X):
            for y in range(0, tamanho_Y):
                if y == 0:
                    self.quadrado[x] = {}

                imgBolinhaNoClick = self.images["bolinhaNoClick"]

                quadrado = {
                    "id": id,
                    "state": bolinhaNoClick,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "button": Button(self.frame, image = imgBolinhaNoClick)
                }

                quadrado["button"].bind(buttom_click, self.selecionaBolinha(x, y))
                quadrado["button"].grid( row = x+1, column = y )

                self.quadrado[x][y] = quadrado

    def selecionaBolinha(self, x, y):
        return lambda Button: self.clickBolinha(self.quadrado[x][y])

    def clickBolinha(self, quadrado):
        if self.inicioTempo == None:
            self.inicioTempo = datetime.now()
            self.updateTimer()
        if quadrado["state"] != bolinhaClick:
            quadrado["button"].config(image = self.images["bolinhaClick"])
            quadrado["state"] = bolinhaClick
            self.acertos += 1
            self.labels["Acertos"].config(text = "Acertos: "+str(self.acertos))

    def restart(self):
        self.iniciar()
        self.atualizar()

    def atualizar(self):
        self.labels["Tentativas"].config(text = "Tentativas: " + str(self.tentativas) + " de "+ str(varTentativas))
        self.labels["Acertos"].config(text = "Acertos: "+str(self.acertos))
        self.labels["Total"].config(text = "Total: "+str(self.total))
        self.labels["Tempo"].config(text = "00:00:00")

    def gameOver(self, tempo):

        self.tk.update()

        msg = "Seu resultado foi: \n Acertos: " + str(self.acertos) + "\n Tempo: " + str(tempo) + "\n Total: " + str(self.total) + "\n Deseja salvar os resultados?"
        salvar = "Acertos: " + str(self.acertos) + " - Tempo: " + str(tempo) + " - Total: " + str(self.total)
        write = str(self.acertos) + "," + str(tempo) + "," + str(self.total) + "\n"

        res = tkMessageBox.askyesno("Sim - Salvar no Ranking. \n Não - Reiniciar sem salvar", msg)
        if res:
            rankingSalvar(salvar)
            rankingLog(write)
            self.restart()
        else:
            self.restart()

    def updateTimer(self):
        ts = "00:00:00"
        if self.inicioTempo != None:
            delta = datetime.now() - self.inicioTempo
            ts = str(delta).split('.')[0]
            if delta.total_seconds() < 36000:
                ts = "0" + ts # zero-pad
        self.labels["Tempo"].config(text = ts)
        tempoPercorrido = int(ts[7:8])
        if tempoPercorrido >= varTempo:
            self.gameOver(tempoPercorrido)
        else:
            self.frame.after(100, self.updateTimer)


def rankingExport():
    with open('Projeto\\log.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open('Projeto\\Ranking.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('acertos', 'tempo', 'total'))
            writer.writerows(lines)

def rankingSalvar(mensagem):
    with open('Projeto\\ranking.txt', 'a') as file:
        file.write(mensagem)

def rankingLog(mensagem):
    with open('Projeto\\log.txt', 'a') as file:
        file.write(mensagem)

def rankingVisualiza():
    print("hello")

def rankingLimpa():
    print("hello")

def novoJogo():
    clickColor.__init__

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

menu_novoJogo = Menu(meu_menu, tearoff=0)
menu_configuracao = Menu(meu_menu, tearoff=0)
menu_configuracao.add_command(label="Dificuldade", command=selecionarDificuldade)
menu_configuracao.add_command(label="Geral", command=configuracao)
menu_ranking = Menu(meu_menu, tearoff=0)
menu_ranking.add_command(label="Planilha", command=rankingExport)
menu_ranking.add_command(label="Visualizar", command=rankingVisualiza)
menu_ranking.add_separator()
menu_ranking.add_command(label="Apagar", command=rankingLimpa)

meu_menu.add_cascade(label="Novo Jogo", command=novoJogo())
meu_menu.add_cascade(label="Configuração", menu=menu_configuracao)
meu_menu.add_cascade(label="Ranking", menu=menu_ranking)

nuvem = PhotoImage(file = os.path.join(diretorio, 'img\\nuvem.png'))
nuvem2 = PhotoImage(file= os.path.join(diretorio, 'img\\nuvem2.png'))
imgBolinhaClick = PhotoImage(file= os.path.join(diretorio, 'img\\bolinhaClick.png'))
imgBolinhaNoClick = PhotoImage(file= os.path.join(diretorio, 'img\\bolinhaNoClick.png'))

logo = Label(janela, justify=LEFT, compound = CENTER, padx = 5, image=nuvem, font=("Calibri", 25)).pack(side="left",anchor=NW)
dificuldade = Label(janela, justify=LEFT, compound = CENTER, padx = 5, text="Dificuldade", image=nuvem2, font=("Calibri", 25), textvariable=varDificuldade).pack(side="right",anchor=NE)
colorReact = clickColor(janela)

janela.mainloop()