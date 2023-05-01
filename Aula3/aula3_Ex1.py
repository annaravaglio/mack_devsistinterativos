import tkinter as tk

janela = tk.Tk()
janela.title("Testando CheckButton")
janela.geometry("400x200")

var1 = tk.IntVar()
var2 = tk.IntVar()

def selecao():
    if var1.get() == 1 and var2.get() == 0:
        lb.config(text="Opção 1")
    elif var1.get() == 0 and var2.get() == 1:
        lb.config(text="Opção 2")
    elif var1.get() == 1 and var2.get() == 1:
        lb.config(text="Opção 1 e 2")
    else:
        lb.config(text="Nenhuma das opções")

cb1 = tk.Checkbutton(janela, text="Opção 1", onvalue=1, offvalue=0, variable=var1, command=selecao)
cb1.pack(anchor=tk.W)
cb2 = tk.Checkbutton(janela, text="Opção 2", onvalue=1, offvalue=0, variable=var2, command=selecao)
cb2.pack(anchor=tk.W)

lb = tk.Label(janela, text="")
lb.pack(anchor=tk.W)

janela.mainloop()

