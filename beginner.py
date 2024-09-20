import customtkinter as ctk
from PIL import Image
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

    def teste(self):
        url = "https://www.google.com/search?q=Balisong"
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
        
        
        self.botao(self.root, "teste", "JetBrains Mono", 20, 240, 40, "Dark Blue", "White", self.teste, 0.5, 0.5, "c")


        self.root.mainloop()

if __name__ == "__main__":
    Begginer().Start_Begginer()
