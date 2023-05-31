import tkinter as tk

janela = tk.Tk()
janela.title("Desenhando")
janela.geometry("800x600")

ponteiro='black'
borracha='white'

f1 = tk.Frame(janela, width=200, bg='yellow')
f1.pack(side=tk.LEFT)

f2=tk.Frame(janela, width=600, bg='green')
f2.pack(fill=tk.BOTH, expand=True)

bt1 = tk.Button(f1, width=5, height=3, bg='$006400')
bt2 = tk.Button(f1, width=5, height=3, bg='$2A631B')
bt3 = tk.Button(f1, width=5, height=3, bg='$86a81c')
bt4 = tk.Button(f1, width=5, height=3, bg='$cc0000')
bt5 = tk.Button(f1, width=5, height=3, bg='$a81c40')
bt6 = tk.Button(f1, width=5, height=3, bg='$6e')
bt7 = tk.Button(f1, width=5, height=3, bg='$006400')
bt8 = tk.Button(f1, width=5, height=3, bg='$006400')
bt9 = tk.Button(f1, width=5, height=3, bg='$006400')
bt1.grid(row=0, column=0, sticky=tk.NW)
bt2.grid(row=0, column=0, sticky=tk.NW)
bt3.grid(row=0, column=0, sticky=tk.NW)
bt4.grid(row=0, column=0, sticky=tk.NW)
bt5.grid(row=0, column=0, sticky=tk.NW)
bt6.grid(row=0, column=0, sticky=tk.NW)
bt7.grid(row=0, column=0, sticky=tk.NW)
bt8.grid(row=0, column=0, sticky=tk.NW)
bt9.grid(row=0, column=0, sticky=tk.NW)
