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

    def abrirTutorial(self, link):
        url = link
        webbrowser.open(url, new=0, autoraise=True)

    def basePath(self):
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    def texto(self, master, text, font, size, relx, rely, anchor):
        texto = ctk.CTkLabel(master, text=text, font=(font, size))
        texto.place(relx=relx, rely=rely, anchor=anchor)

    def botao(self, master, text, font, size, width, height, color, text_color, command, relx, rely, anchor):
        botao = ctk.CTkButton(master, text=text, width=width, height=height,
                               font=(font, size), fg_color=color, text_color=text_color, command=command)
        botao.place(relx=relx, rely=rely, anchor=anchor)
        return botao

    def imagem(self, name, master, relx, rely, anchor, x, y):
        imagem = ctk.CTkImage(Image.open(f"{self.basePath()}/{name}"), size=(x, y))
        imagem_place = ctk.CTkLabel(master, image=imagem, text='')
        imagem_place.place(relx=relx, rely=rely, anchor=anchor)

    def Start_Begginer(self):
        frame = ctk.CTkScrollableFrame(self.root, width=200, height=200)
        
        self.botao(self.root, "Basic opening", "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[0]}"), 0.2, 0.2, "c")

        self.botao(self.root, "The Fan", "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[1]}"), 0.45, 0.2, "c")

        self.botao(self.root, "2 Reverses", "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[2]}"), 0.68, 0.2, "c")



        self.root.mainloop()

if __name__ == "__main__":
    Begginer().Start_Begginer()
