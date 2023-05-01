import tkinter as tk

janela = tk.Tk()
janela.title("Testando RadioButton")
janela.geometry("400x200")

var1 = tk.IntVar()

def selecao():
    texto = "Você selecionou a opção " + str(var1.get())
    lb.config(text=texto)

rb1 = tk.Radiobutton(janela, text="Opção 1", value=1, variable=var1, command=selecao)
rb1.pack(anchor=tk.W)

rb2 = tk.Radiobutton(janela, text="Opção 2", value=2, variable=var1, command=selecao)
rb2.pack(anchor=tk.W)

rb3 = tk.Radiobutton(janela, text="Opção 3", value=3, variable=var1, command=selecao)
rb3.pack(anchor=tk.W)

lb = tk.Label(janela, text="")
lb.pack(anchor=tk.W)

janela.mainloop()

