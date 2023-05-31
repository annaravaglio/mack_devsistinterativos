import tkinter as tk
from tkinter.ttk import Scale

janela = tk.Tk()
janela.title("Desenhando")
janela.geometry("800x600")

ponteiro='black'
borracha='white'

def desenhar(button_press):
    if button_press==1:
        ponteiro='#006400'
    if button_press==2:
        ponteiro='#2A631B'
    if button_press==3:
        ponteiro='#2A631B'
    if button_press==4:
        ponteiro='#cc0000'
        
    #como pegar movimento do mouse e atualizar o canvas
    #para casa

    canvas.create_oval(5,5,5,5, fill=ponteiro, outline=ponteiro,
                       width=5)

f1 = tk.Frame(janela, width=200, bg='yellow')
f1.pack(side=tk.LEFT, anchor=tk.NW)

canvas = tk.Canvas(janela, width=600, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

bt1 = tk.Button(f1, width=5, height=3, bg='#006400',
                command= lambda m=1: desenhar(m))
bt1.grid(row=0, column=0, sticky=tk.NW)

bt2 = tk.Button(f1, width=5, height=3, bg='#2A631B',
                command= lambda m=2: desenhar(m),)
bt2.grid(row=0, column=1)

bt3 = tk.Button(f1, width=5, height=3, bg='#86a81c',
                command= lambda m=3: desenhar(m))
bt3.grid(row=0, column=2)

bt4 = tk.Button(f1, width=5, height=3, bg='#cc0000',
                command= lambda m=4: desenhar(m))
bt4.grid(row=1, column=0)

bt5 = tk.Button(f1, width=5, height=3, bg='#a81c40')
bt5.grid(row=1, column=1)

bt6 = tk.Button(f1, width=5, height=3, bg='#6e2626')
bt6.grid(row=1, column=2)

bt7 = tk.Button(f1, width=5, height=3, bg='#03062c')
bt7.grid(row=2, column=0)

bt8 = tk.Button(f1, width=5, height=3, bg='#0f1ee0')
bt8.grid(row=2, column=1)

bt9 = tk.Button(f1, width=5, height=3, bg='#009ce9')
bt9.grid(row=2, column=2)

btn_apagar = tk.Button(f1, text='APAGAR')
btn_apagar.grid(row=3, column=0, columnspan=3, sticky=tk.NSEW)


janela.mainloop()
