import tkinter as tk
from tkinter.scrolledtext import ScrolledText

janela = tk.Tk()
janela.title("Testando Menu Cascata")
janela.geometry("400x200")

def pegaTexto():
    #Pegar da 1.0 (Linha 1, caracter 0) até o final (tk.END)
    conteudo = st.get("1.0", tk.END)
    print(conteudo)

def insereTexto():
    #Pegar da 1.0 (Linha 1, caracter 0) até o final (tk.END)
    texto = "Testando o textarea com scroll\n"
    st.insert("1.0", texto)

#Impedir a janela de crescer
janela.resizable(False,False)
st = ScrolledText(janela, width=50, height=10)
st.pack(fill=tk.X, side=tk.TOP)

bt = tk.Button(janela, text="Inserir Texto", command=insereTexto)
bt.pack(fill=tk.BOTH, expand=True)

janela.mainloop()