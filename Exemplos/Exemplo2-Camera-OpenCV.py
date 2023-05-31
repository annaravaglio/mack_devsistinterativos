# Python program to open the
# camera in Tkinter
import tkinter as tk
import cv2
from PIL import Image, ImageTk

janela = tk.Tk()

#Define um objeto de captura de vídeo
video = cv2.VideoCapture(0)
  
#Declara a largura e a altura do frame de video
width, height = 800, 600
video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  
#Vincula a tecla ESC para fechar janela
janela.bind('<Escape>', lambda e: janela.quit())


def abrir_camera():  
    #Captura frame por frame
    _, frame = video.read()
    
    #Converte a imagem de um espaço de cores para outro
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
  
    #Captura o último frame e transforma em imagem
    captured_image = Image.fromarray(opencv_image)
  
    #Converte a imagem capturada para photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)
  
    #Exibindo fotoimagem na label
    label_widget.photo_image = photo_image
  
    #Configura a imagem na label
    label_widget.configure(image=photo_image)
  
    #Repete o mesmo processo a cada 10 segundos
    label_widget.after(10, abrir_camera)
    
#Cria a interface com widgets
label_widget = tk.Label(janela)
label_widget.pack()
bt1 = tk.Button(janela, text="Abrir Camera", command=abrir_camera)
bt1.pack()

janela.mainloop()
