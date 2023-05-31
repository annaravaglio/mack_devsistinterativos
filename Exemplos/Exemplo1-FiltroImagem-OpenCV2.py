import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image,ImageTk #Pillow
import cv2 #OpenCV
import imutils #Editar imagens
import numpy as np 

janela = tk.Tk()
janela.title("Aplicando filtro de cores")

def carregar_imagem():    
    path_image = fd.askopenfilename(filetypes = [
        ("image", ".jpeg"),
        ("image", ".png")])

    if len(path_image) > 0:
        global image

        #Ler e redimensionar imagem de entrada
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=380)
        imageToShow = imutils.resize(image, width=180)
        
        #Converter a imagem BGR(openCV) para RGB(Pillow)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)
        
        #Visualizar a imagem de entrada na GUI
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)
        lblInputImage.configure(image=img)
        lblInputImage.image = img

        #Label "IMAGEM DE ENTRADA"
        lblInfo1 = tk.Label(janela, text="IMAGEM DE ENTRADA:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

        #Quando carregar a imagem de entrada, esvaziar a imagem de saída
        #e limpar a seleção dos radiobuttons
        lblOutputImage.image = ""
        selecionado.set(0)

def filtro_cor():    
    #detectar a opção radio selecionada e definir espectro de cores
    if selecionado.get() == 1:
        #Vermelho
        limiteBaixo1 = np.array([0, 140, 90], np.uint8)
        limiteAlto1 = np.array([8, 255, 255], np.uint8)
        limiteBaixo2 = np.array([160, 140, 90], np.uint8)
        limiteAlto2 = np.array([180, 255, 255], np.uint8)
    if selecionado.get() == 2:
        #Amarelo
        limiteBaixo = np.array([10, 98, 0], np.uint8)
        limiteAlto = np.array([25, 255, 255], np.uint8)
    if selecionado.get() == 3:
        #Azul celeste
        limiteBaixo = np.array([88, 104, 121], np.uint8)
        limiteAlto = np.array([99, 255, 243], np.uint8)

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageGray = cv2.cvtColor(imageGray, cv2.COLOR_GRAY2BGR)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    if selecionado.get() == 1:
        #Detecta a cor vermelha
        maskVermelha1 = cv2.inRange(imageHSV, limiteBaixo1, limiteAlto1)
        maskVermelha2 = cv2.inRange(imageHSV, limiteBaixo2, limiteAlto2)
        mask = cv2.add(maskVermelha1, maskVermelha2)
    else:
        #Detecta cor amarela e Azul celeste
        mask = cv2.inRange(imageHSV, limiteBaixo, limiteAlto)
        
    mask = cv2.medianBlur(mask, 7)
    colorDetected = cv2.bitwise_and(image, image, mask=mask)

    #Fundo em cinza
    invMask = cv2.bitwise_not(mask)
    bgGray = cv2.bitwise_and(imageGray, imageGray, mask=invMask)

    #Somar bgGray com colorDetected
    finalImage = cv2.add(bgGray, colorDetected)
    imageToShowOutput = cv2.cvtColor(finalImage, cv2.COLOR_BGR2RGB)
    
    #Visualizar a imagem na label lblOutputImage
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    lblOutputImage.configure(image=img)
    lblOutputImage.image = img

    # Label IMAGEN DE SALIDA
    lblInfo3 = tk.Label(janela, text="IMAGEM DE SAIDA", font="bold")
    lblInfo3.grid(column=1, row=0, padx=5, pady=5)


#Cria um botão para carregar a imagem de entrada
btn = tk.Button(janela, text="Carregar imagem", width=25, command=carregar_imagem)
btn.grid(row=0, column=0, padx=5, pady=5)

#Label para apresentar a imagem de entrada
lblInputImage = tk.Label(janela)
lblInputImage.grid(row=2, column=0)

#Label para apresentar a imagem de saída
lblOutputImage = tk.Label(janela)
lblOutputImage.grid(row=2, column=1, rowspan=6)

#Label "Selecione a cor a destacar"
lblInfo = tk.Label(janela, text="Selecione a cor a destacar", width=25)
lblInfo.grid(row=3, column=0, padx=5, pady=5)

#Radiobuttons com as opções das cores
selecionado = tk.IntVar()
rad1 = tk.Radiobutton(janela, text='Vermelho', width=25,value=1, variable=selecionado, command=filtro_cor)
rad2 = tk.Radiobutton(janela, text='Amarelo', width=25, value=2, variable=selecionado, command=filtro_cor)
rad3 = tk.Radiobutton(janela, text='Azul', width=25, value=3, variable=selecionado, command=filtro_cor)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)

janela.mainloop()
