import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title('Exemplo Imagens')
janela.geometry('400x250')

canvas = tk.Canvas(janela, width=200, height=250)
canvas.pack()

bt = tk.Button(janela, text="Clique Aqui" )
bt.pack()

#carregando a imagem
img = (Image.open("joaninha.png"))

#Redimensionando a imagem
imagem_redimensionada = img.resize((150,150), Image.Resampling.LANCZOS)
nova_imagem = ImageTk.PhotoImage(imagem_redimensionada)

canvas.create_image(10, 10, anchor=tk.NW, image=nova_imagem)

janela.mainloop()


