import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, Canvas, Frame, BOTH
from random import randint
from PIL import Image, ImageTk
import cv2

varDificuldade = 0
varCorClick = "#000000"
varCorNoClick = "#FFFFFF"
varQtdBolinhas = 100
varCores = 0
varTentativas = 5

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
def selecionarDificuldade():
    win = tk.Toplevel() #Subjanela
    win.title("Dificuldade")
    win.geometry("300x100")

def configuracao():
    print("hello")

def bolinha():
    canvas = Canvas()
    canvas.create_oval(10, 10, 50, 50, fill=varCorNoClick)
    canvas.pack(fill=BOTH, expand=1)

janela = tk.Tk()
janela.title("Projeto - colorReact")
janela.geometry("1024x600")
janela.resizable(False, False)

meu_menu = tk.Menu(janela)
janela.config(menu=meu_menu)

menu_novoJogo = tk.Menu(meu_menu, tearoff=0)
menu_dificuldade = tk.Menu(meu_menu, tearoff=0)
menu_ranking = tk.Menu(meu_menu, tearoff=0)
menu_ranking.add_command(label="Planilha", command=rankingExport)
menu_ranking.add_command(label="Visualizar", command=rankingVisualiza)
menu_ranking.add_separator()
menu_ranking.add_command(label="Apagar", command=rankingLimpa)
menu_configuracao = tk.Menu(meu_menu, tearoff=0)

meu_menu.add_cascade(label="Novo Jogo", menu=menu_novoJogo, command=novoJogo)
meu_menu.add_cascade(label="Dificuldade", menu=menu_dificuldade, command=selecionarDificuldade)
meu_menu.add_cascade(label="Ranking", menu=menu_ranking)
meu_menu.add_cascade(label="Configuração", menu=menu_dificuldade, command=configuracao)

nuvem = tk.PhotoImage(file="E:\\GitHub\\mack_devsistinterativos\\Projeto\\img\\nuvem.png")
nuvem2 = tk.PhotoImage(file="E:\\GitHub\\mack_devsistinterativos\\Projeto\\img\\nuvem2.png")

logo = tk.Label(janela, justify=tk.LEFT, compound = tk.CENTER, padx = 5, image=nuvem, font=("Calibri", 25)).pack(side="left",anchor=tk.NW)
iniciar = tk.Button(janela, text="Iniciar", font=("Calibri", 25), command=iniciarJogo).pack(side="top",anchor=tk.N)
dificuldade = tk.Label(janela, justify=tk.LEFT, compound = tk.CENTER, padx = 5, text="Dificuldade", image=nuvem2, font=("Calibri", 25), textvariable=varDificuldade).pack(side="right",anchor=tk.NE)

telaBolinhas = tk.Frame(janela, bd = 2, height=413, width=747, bg="#FFFFFF")
imgBolinha=bolinha()
for i in range(5):
    for j in range(20):
        # imgBolinha=bolinha()
        buttonBolinha = tk.Button(telaBolinhas, image=imgBolinha,width=1, height=1, command= bolinha()).grid(row=i, column=j)
telaBolinhas.pack(side="left",anchor=tk.SW)
# img = Image.open(r"E:\GitHub\mack_devsistinterativos\Projeto\img\nuvem2.png")
# nuvem = ImageTk.PhotoImage(img)
# canvas = tk.Canvas(janela)
# canvas.pack()
# canvas.create_image(1024, 1024, anchor=tk.NE, image=nuvem)

# label1 = tk.Label( janela, text = "Welcome", image = nuvem)
# label1.place(x = 0,y = 0)

# img = tk.PhotoImage(file="E:\\GitHub\\mack_devsistinterativos\\Projeto\\img\\nuvem2.png")
# labDificuldade = tk.Label(janela, text="Dificuldade")

# labDificuldade["compound"] = tk.CENTER
# labDificuldade["image"] = img
# labDificuldade.grid(row=0, column=2,columnspan=3,sticky=tk.NE)

janela.mainloop()