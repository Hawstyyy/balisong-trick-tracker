import customtkinter as ctk
from PIL import Image
from getvideos import url
import os
import sys
import webbrowser


class Begginer:
    def __init__(self) -> None:
        self.root = ctk.CTkToplevel()
        self.root.geometry("1024x620")
        self.root.resizable(False, False)
        self.root.title("Balisong Flipping Tracker")
        self.root.iconbitmap(f"{self.basePath()}/logo.ico")
        self.frame = ctk.CTkScrollableFrame(self.root, width=1000, height=620)
        self.frame.place(relx=0.5, rely=0.5, anchor='c')

    def abrirTutorial(self, link):
        url = link
        webbrowser.open(url, new=0, autoraise=True)

    def basePath(self):
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    def texto(self, master, text, font, size, relx, rely, anchor):
        texto = ctk.CTkLabel(master, text=text, font=(font, size))
        texto.place(relx=relx, rely=rely, anchor=anchor)

    def botao(self, master, text, font, size, width, height, color, text_color, command, x, y):
        botao = ctk.CTkButton(master, text=text, width=width, height=height,
                               font=(font, size), fg_color=color, text_color=text_color, command=command)
        botao.place(x=x, y=y)
        return botao

    def imagem(self, name, master, relx, rely, anchor, x, y):
        imagem = ctk.CTkImage(Image.open(f"{self.basePath()}/{name}"), size=(x, y))
        imagem_place = ctk.CTkLabel(master, image=imagem, text='')
        imagem_place.place(relx=relx, rely=rely, anchor=anchor)

    def Start_Begginer(self):

        x = 128
        y = 69
        for i in range(0, len(url)):
            if x >= 656 or i == 0:
                x = 128
                if i != 0:
                    y += 60
            else:
                x += 264
    
            self.botao(self.frame, url[i]["titulo"], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda i=i: self.abrirTutorial(url[i]["link"]), x, y)

        self.root.mainloop()

if __name__ == "__main__":
    Begginer().Start_Begginer()
