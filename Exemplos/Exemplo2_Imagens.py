import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title('Exemplo Imagem Interativa')
janela.geometry('400x250')

#carregando imagens
img1 = (Image.open("joaninha.png"))
img2 = (Image.open("bug.png"))
img3 = (Image.open("nofoto.png"))

#Redimensionando imagens
img1Red = img1.resize((150,150), Image.Resampling.LANCZOS)
img2Red = img2.resize((150,150), Image.Resampling.LANCZOS)
img3Red = img3.resize((150,150), Image.Resampling.LANCZOS)

nova_img1Red = ImageTk.PhotoImage(img1Red)
nova_img2Red = ImageTk.PhotoImage(img2Red)
nova_img3Red = ImageTk.PhotoImage(img3Red)

canvas = tk.Canvas(janela, width=400, height=180, bg="green")
canvas.pack()
canvas.create_image(10, 10, anchor=tk.NW, image=nova_img3Red)

def imagem1():
    canvas.delete('all')
    canvas.create_image(10, 10, anchor=tk.NW, image=nova_img2Red)
               
def imagem2():
    canvas.delete('all')
    canvas.create_image(10, 10, anchor=tk.NW, image=nova_img1Red)

bt1 = tk.Button(janela, text="Imagem 1", command=imagem1)
bt1.pack(fill=tk.BOTH, expand=True)

bt2 = tk.Button(janela, text="Imagem 2", command=imagem2)
bt2.pack(fill=tk.BOTH, expand=True)

janela.mainloop()


