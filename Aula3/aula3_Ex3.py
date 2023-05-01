import tkinter as tk

janela = tk.Tk()
janela.title("Testando Menu Cascata")
janela.geometry("400x200")

#Funções vem antes de tudo pois são chamadas depois, variáveis tem que ser globais pois as funções não recebem/enviam retornos
def abreJanela():
    win = tk.Toplevel() #Subjanela
    win.title("SubJanela")
    win.geometry("200x100")

    lb = tk.Label(win, text="Hello World!! <3")
    lb.pack()

def fecharJanela():
    janela.destroy()

#Criando menu
meu_menu = tk.Menu(janela)
janela.config(menu=meu_menu)

#Subitens: sempre tem que ser declarados antes dos itens, pois são encapsulados depois
#Mesmo dizendo que é o pai, tem que colocar no menu o cascade para inserir menu em cascata
menu_arquivo = tk.Menu(meu_menu, tearoff=0)
menu_arquivo.add_command(label="Novo", command=abreJanela)
menu_arquivo.add_command(label="Abrir")
menu_arquivo.add_command(label="Salvar")
menu_arquivo.add_command(label="Salvar como...")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Fechar", command=fecharJanela)

menu_editar = tk.Menu(meu_menu, tearoff=0)
menu_editar.add_command(label="Desfazer")
menu_editar.add_separator()
menu_editar.add_command(label="Recortar")
menu_editar.add_command(label="Copiar")
menu_editar.add_command(label="Colar")
menu_editar.add_command(label="Deletar")
menu_editar.add_command(label="Selecionar tudo")

menu_ajuda = tk.Menu(meu_menu, tearoff=0)
menu_ajuda.add_command(label="Ajuda")
menu_ajuda.add_separator()
menu_ajuda.add_command(label="Sobre")

#Adicionando Itens no menu
# meu_menu.add_command(label="Arquivo")
# meu_menu.add_command(label="Editar")
# meu_menu.add_command(label="Ajuda")
meu_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
meu_menu.add_cascade(label="Editar", menu=menu_editar)
meu_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

janela.mainloop()