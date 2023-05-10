import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

janela = tk.Tk()
janela.title("EAD 1 - Anna Ravaglio")
janela.minsize(300, 250)
janela.resizable(True, True)

varHamburger = tk.IntVar()
varHotDog = tk.IntVar()
varQueijoQuente = tk.IntVar()
varBatataFrita = tk.IntVar()
varNuggets = tk.IntVar()
varMaionese = tk.IntVar()
varPagamento = tk.IntVar()
valorTotal = tk.IntVar()

lista_Hamburger = []
lista_HotDog = []
lista_QueijoQuente = []
lista_BatataFrita = []
lista_Nuggets = []
lista_Maionese = []
lista_Pagamento = []

def confirmarPedido():
    if varPagamento.get() == 0 :
        messagebox.showerror("Erro", "Selecione a forma de pagamento!")
    else:
        lista_Pagamento.append(varPagamento.get())
        if varHamburger.get() == 0 and varHotDog.get() == 0 and varQueijoQuente.get() == 0 and varBatataFrita.get() == 0 and varNuggets.get() == 0 and varMaionese.get() == 0:
            messagebox.showerror("Erro", "Selecione algum item do menu!")
        if varHamburger.get() == 1:
            lista_Hamburger.append(10)
        else:
            lista_Hamburger.append(0)
        if varHotDog.get() == 1:
            lista_HotDog.append(8)
        else:
            lista_HotDog.append(0)    
        if varQueijoQuente.get() == 1:
            lista_QueijoQuente.append(5)
        else:
            lista_QueijoQuente.append(0)
        if varBatataFrita.get() == 1:
            lista_BatataFrita.append(8)
        else:
            lista_BatataFrita.append(0)
        if varNuggets.get() == 1:
            lista_Nuggets.append(10)
        else:
            lista_Nuggets.append(0)
        if varMaionese.get() == 1:
            lista_Maionese.append(2)
        else:
            lista_Maionese.append(0)

    print(lista_Hamburger)
    print(lista_HotDog)
    print(lista_QueijoQuente)
    print(lista_BatataFrita)
    print(lista_Nuggets)
    print(lista_Maionese)
    print(lista_Pagamento)

def abreConfirmacao():
    messagebox.showinfo("Sucesso", "Pedido realizada com sucesso!!")

def fecharJanela():
    janela.destroy()

def resumoPedido():
    
    valorTotal = 0
    texto = ""
    resumo.delete('1.0', tk.END)

    if varHamburger.get() == 0 and varHotDog.get() == 0 and varQueijoQuente.get() == 0 and varBatataFrita.get() == 0 and varNuggets.get() == 0 and varMaionese.get() == 0:
        messagebox.showerror("Erro", "Selecione algum item do menu!")

    if varHamburger.get() == 1:
        texto = texto + "Hamburguer = R$10\n"
        valorTotal = valorTotal + 10
    if varHotDog.get() == 1:
        texto = texto + "Hot Dog = R$8\n"
        valorTotal = valorTotal + 8
    if varQueijoQuente.get() == 1:
        texto = texto + "Queijo Quente = R$5\n"
        valorTotal = valorTotal + 5
    if varBatataFrita.get() == 1:
        texto = texto + "Batata Frita = R$8\n"
        valorTotal = valorTotal + 8
    if varNuggets.get() == 1:
        texto = texto + "Nuggets = R$10\n"
        valorTotal = valorTotal + 10
    if varMaionese.get() == 1:
        texto = texto + "Maionese = R$2\n"
        valorTotal = valorTotal + 5

    texto = texto + "Total do Pedido - R$ " + str(valorTotal) + "\n"

    resumo.pack(fill=tk.X, side=tk.TOP) 
    resumo.insert("1.0", texto)

meu_menu = tk.Menu(janela)
janela.config(menu=meu_menu)

menu_pedidos = tk.Menu(meu_menu, tearoff=0)
menu_pedidos.add_command(label="Meus Pedidos")
menu_pedidos.add_command(label="Minha Conta")
menu_pedidos.add_command(label="Contato")
menu_pedidos.add_separator()
menu_pedidos.add_command(label="Sair", command=fecharJanela)

meu_menu.add_cascade(label="Pedidos", menu=menu_pedidos)

lbNome = tk.Label(janela, text="Tabela de valores")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Pratos:")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Hamburguer - R$ 10 | Hot Dog - R$ 8 | Queijo Quente - R$ 5")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Acompanhamentos:")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Batata Frita - R$ 8 | Nuggets - R$ 10 | Maionese - R$ 2")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Faça seu pedido!")
lbNome.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Pratos:")
lbNome.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Hamburguer", onvalue=1, offvalue=0, variable=varHamburger, command=resumoPedido)
cb1.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Hot Dog", onvalue=1, offvalue=0, variable=varHotDog, command=resumoPedido)
cb1.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Queijo Quente", onvalue=1, offvalue=0, variable=varQueijoQuente, command=resumoPedido)
cb1.pack(anchor=tk.W)

lbNome = tk.Label(janela, text="Acompanhamentos:")
lbNome.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Batata Frita", onvalue=1, offvalue=0, variable=varBatataFrita, command=resumoPedido)
cb1.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Nuggets", onvalue=1, offvalue=0, variable=varNuggets, command=resumoPedido)
cb1.pack(anchor=tk.W)
cb1 = tk.Checkbutton(janela, text="Maionese", onvalue=1, offvalue=0, variable=varMaionese, command=resumoPedido)
cb1.pack(anchor=tk.W)

rbCredito = tk.Radiobutton(janela, text="Cartão de Crédito", value=1, variable=varPagamento)
rbCredito.pack(anchor=tk.W)

rbDebito = tk.Radiobutton(janela, text="Cartão de Débito", value=2, variable=varPagamento)
rbDebito.pack(anchor=tk.W)

rbDinheiro = tk.Radiobutton(janela, text="Dinheiro", value=3, variable=varPagamento)
rbDinheiro.pack(anchor=tk.W)

resumo = ScrolledText(janela, width=50, height=10)

btConfirmar = tk.Button(janela, text="Confirmar Pedido", command=confirmarPedido)
btConfirmar.pack(anchor=tk.W, expand=True)

lbConfirmar = tk.Label(janela, text="Pedido confirmado")

janela.mainloop()