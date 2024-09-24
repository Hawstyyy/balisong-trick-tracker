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
        frame = ctk.CTkScrollableFrame(self.root, width=1000, height=620)
        frame.place(relx=0.5, rely=0.5, anchor='c')
        x = 128
        y = 69
        for i in range(0, len(url)):
            if x >= 656 or i == 0:
                x = 128
                if i != 0:
                    y += 60
            else:
                x += 264
    
            self.botao(frame, url[i]["titulo"], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda i=i: self.abrirTutorial(url[i]["link"]), x, y)


        # self.botao(self.root, url[1], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[1]}"), 392, 69)

        # self.botao(self.root, url[2], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[2]}"), 656, 69)

        # self.botao(self.root, url[3], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[3]}"), 128, 129)

        # self.botao(self.root, url[4], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[4]}"), 392, 129)

        # self.botao(self.root, url[5], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[5]}"), 656, 129)

        # self.botao(self.root, url[6], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[6]}"), 128, 189)

        # self.botao(self.root, url[7], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[7]}"), 392, 189)

        # self.botao(self.root, url[8], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[8]}"), 656, 189)

        # self.botao(self.root, url[9], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[9]}"), 128, 249)

        # self.botao(self.root, url[10], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[10]}"), 392, 249)

        # self.botao(self.root, url[11], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[11]}"), 656, 249)

        # self.botao(self.root, url[12], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[12]}"), 128, 309)

        # self.botao(self.root, url[13], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[13]}"), 392, 309)

        # self.botao(self.root, url[14], "JetBrains Mono", 20, 240, 40, "Blue", "White", lambda: self.abrirTutorial(f"{url[14]}"), 656, 309)


        self.root.mainloop()

if __name__ == "__main__":
    Begginer().Start_Begginer()
