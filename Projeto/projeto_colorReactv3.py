# Python Version 2.7.3
# File: minesweeper.py

from tkinter import *
from tkinter import messagebox as tkMessageBox
from collections import deque
import random
import platform
import time
from datetime import time, date, datetime

tamanho_X = 10
tamanho_Y = 10

noClick = 0
click = 1

buttom_click = "<Button-1>"

window = None

class Minesweeper:

    def __init__(self, tk):

        self.images = {
            "bolinhaNoClick": PhotoImage(file = "E:\\GitHub\\mack_devsistinterativos\\Projeto\\img\\bolinhaNoClick.png"),
            "bolinhaClick": PhotoImage(file = "E:\\GitHub\\mack_devsistinterativos\\Projeto\\img\\bolinhaClick.png")
        }

        # set up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # set up labels/UI
        self.labels = {
            "Tempo": Label(self.frame, text = "00:00:00"),
            "Tentativas": Label(self.frame, text = "Tentativas: 1 de 5"),
            "Acertos": Label(self.frame, text = "Acertos: 0 "),
            "Total": Label(self.frame, text = "Total: 100")
        }
        self.labels["Tempo"].grid(row = 0, column = 0, columnspan = tamanho_Y) # top full width
        self.labels["Tentativas"].grid(row = tamanho_X+1, column = 0, columnspan = int(tamanho_Y/2)) # bottom left
        self.labels["Acertos"].grid(row = tamanho_X+1, column = int(tamanho_Y/2)-1, columnspan = int(tamanho_Y/2)) # bottom right
        self.labels["Total"].grid(row = tamanho_X+1, column = int(tamanho_Y/2)-1, columnspan = int(tamanho_Y/2)) # bottom right

        self.restart() # start game
        self.updateTimer() # init timer

    def setup(self):
        # create flag and clicked tile variables
        self.acertos = 0
        self.total = 0
        self.tentativas = 0
        self.startTime = None

        # create buttons
        self.tiles = dict({})
        self.mines = 0
        for x in range(0, tamanho_X):
            for y in range(0, tamanho_Y):
                if y == 0:
                    self.tiles[x] = {}

                id = str(x) + "_" + str(y)
                isMine = False

                # tile image changeable for debug reasons:
                gfx = self.images["bolinhaNoClick"]

                # currently random amount of mines
                tile = {
                    "id": id,
                    "state": noClick,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "button": Button(self.frame, image = gfx)
                }

                tile["button"].bind(buttom_click, self.onClickWrapper(x, y))
                tile["button"].grid( row = x+1, column = y ) # offset by 1 row for timer

                self.tiles[x][y] = tile

    def restart(self):
        self.setup()
        self.refreshLabels()

    def refreshLabels(self):
        self.labels["Tentativas"].config(text = "Tentativas: "+str(self.tentativas))
        self.labels["Acertos"].config(text = "Acertos: "+str(self.acertos))
        self.labels["Total"].config(text = "Total: "+str(self.total))

    def gameOver(self, won):

        self.tk.update()

        msg = "You Win! Play again?" if won else "You Lose! Play again?"
        res = tkMessageBox.askyesno("Game Over", msg)
        if res:
            self.restart()
        else:
            self.tk.quit()

    def updateTimer(self):
        ts = "00:00:00"
        if self.startTime != None:
            delta = datetime.now() - self.startTime
            ts = str(delta).split('.')[0] # drop ms
            if delta.total_seconds() < 36000:
                ts = "0" + ts # zero-pad
        self.labels["Tempo"].config(text = ts)
        self.frame.after(100, self.updateTimer)

    def onClickWrapper(self, x, y):
        return lambda Button: self.onClick(self.tiles[x][y])

    def onClick(self, tile):
        if self.startTime == None:
            self.startTime = datetime.now()

        if tile["state"] != click:
            tile["button"].config(image = self.images["bolinhaClick"])
            tile["state"] = click
            self.acertos += 1

def main():
    # create Tk instance
    window = Tk()
    # set program title
    window.title("Minesweeper")
    # create game instance
    minesweeper = Minesweeper(window)
    # run event loop
    window.mainloop()

if __name__ == "__main__":
    main()
