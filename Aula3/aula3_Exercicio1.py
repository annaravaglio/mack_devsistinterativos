import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

janela = tk.Tk()
janela.title("Exercícío 1 - Anna Ravaglio")
janela.geometry("350x200")
janela.minsize(300, 250)
janela.resizable(True, True)

varGenero = tk.IntVar()
varDisc = tk.IntVar()

lista_Nome = []
lista_Genero = []
lista_Email = []
lista_Disciplina = []

def abreConfirmacao():
    messagebox.showinfo("Sucesso", "Inscrição realizada com sucesso!!")

def fecharJanela():
    janela.destroy()

def cadastrar():
    nome = eNome.get()
    genero = varGenero.get()
    email = eEmail.get()
    disciplina = varDisc.get()

    if len(nome) == 0 or len(email) == 0 or genero == 0 or disciplina == 0:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios")
    else:
        lista_Nome.append(nome)

        if genero == 1:
            lista_Genero.append("F")
        else:
            lista_Genero.append("M")

        lista_Email.append(email)

        if disciplina == 1:
            lista_Disciplina.append("Python")
        elif disciplina == 2:
            lista_Disciplina.append("Java")
        else:
            lista_Disciplina.append("C++")
        abreConfirmacao()

    print(lista_Nome)
    print(lista_Genero)
    print(lista_Email)
    print(lista_Disciplina)

    

def listarTodos():
    win = tk.Toplevel() #Subjanela
    win.title("Listar Todos")
    win.geometry("300x100")

    texto = ""

    st = ScrolledText(win, width=100, height=50)
    
    n = len(lista_Nome)

    for i in range(n):
        texto = texto + lista_Nome[i] + " -- " + lista_Genero[i] + " -- " + lista_Email[i] + " -- " + lista_Disciplina[i] + "\n"
    
    st.pack(fill=tk.X, side=tk.TOP) 
    st.insert("1.0", texto)


def listarPython():
    win = tk.Toplevel() #Subjanela
    win.title("Listar Python")
    win.geometry("300x100")

    texto = ""

    st = ScrolledText(win, width=100, height=50)
    
    n = len(lista_Nome)

    for i in range(n):
        if lista_Disciplina[i] == "Python":
            texto = texto + lista_Nome[i] + " -- " + lista_Genero[i] + " -- " + lista_Email[i] + " -- " + lista_Disciplina[i] + "\n"
        else:
            continue
    
    st.pack(fill=tk.X, side=tk.TOP)
    st.insert("1.0", texto)

def listarJava():
    win = tk.Toplevel() #Subjanela
    win.title("Listar Java")
    win.geometry("300x100")

    texto = ""

    st = ScrolledText(win, width=100, height=50)
    
    n = len(lista_Nome)

    for i in range(n):
        if lista_Disciplina[i] == "Java":
            texto = texto + lista_Nome[i] + " -- " + lista_Genero[i] + " -- " + lista_Email[i] + " -- " + lista_Disciplina[i] + "\n"
        else:
            continue

    st.pack(fill=tk.X, side=tk.TOP)    
    st.insert("1.0", texto)


def listarCpp():
    win = tk.Toplevel() #Subjanela
    win.title("Listar C++")
    win.geometry("300x100")

    texto = ""

    st = ScrolledText(win, width=100, height=50)
    
    n = len(lista_Nome)

    for i in range(n):
        if lista_Disciplina[i] == "C++":
            texto = texto + lista_Nome[i] + " -- " + lista_Genero[i] + " -- " + lista_Email[i] + " -- " + lista_Disciplina[i] + "\n"
        else:
            continue

    st.pack(fill=tk.X, side=tk.TOP)
    st.insert("1.0", texto)

meu_menu = tk.Menu(janela)
janela.config(menu=meu_menu)

menu_listarDisciplina = tk.Menu(meu_menu, tearoff=0)
menu_listarDisciplina.add_command(label="Python", command=listarPython)
menu_listarDisciplina.add_command(label="Java", command=listarJava)
menu_listarDisciplina.add_command(label="C++", command=listarCpp)
menu_listarDisciplina.add_separator()
menu_listarDisciplina.add_command(label="Sair", command=fecharJanela)

meu_menu.add_cascade(label="Listar Todos", command=listarTodos)
meu_menu.add_cascade(label="Listar por Disciplina", menu=menu_listarDisciplina)

lbNome = tk.Label(janela, text="Nome *")
lbNome.pack(anchor=tk.W)

eNome = tk.Entry(janela, width = 25, justify="left", relief="solid")
eNome.pack(anchor=tk.W)

rbFem = tk.Radiobutton(janela, text="Feminino", value=1, variable=varGenero)
rbFem.pack(anchor=tk.W)

rbMasc = tk.Radiobutton(janela, text="Masculino", value=2, variable=varGenero)
rbMasc.pack(anchor=tk.W)

lbEmail = tk.Label(janela, text="E-mail *")
lbEmail.pack(anchor=tk.W)

eEmail = tk.Entry(janela, width = 25, justify="left", relief="solid")
eEmail.pack(anchor=tk.W)

rbPython = tk.Radiobutton(janela, text="Python", value=1, variable=varDisc)
rbPython.pack(anchor=tk.W)

rbJava = tk.Radiobutton(janela, text="Java", value=2, variable=varDisc)
rbJava.pack(anchor=tk.W)

rbCpp = tk.Radiobutton(janela, text="C++", value=3, variable=varDisc)
rbCpp.pack(anchor=tk.W)

btConfirmar = tk.Button(janela, text="Confirmar", command=cadastrar)
btConfirmar.pack(anchor=tk.W, expand=True)

lbConfirmar = tk.Label(janela, text="")

janela.mainloop()