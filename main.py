import customtkinter as ctk
from PIL import Image
import os, sys
from beginner import Begginer

class Main:
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.geometry("1280x720")
    self.root.resizable(False, False)
    self.root.title("Balisong Flipping Tracker")
    self.root.iconbitmap(f"{self.basePath()}/logo.ico")

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))

  def texto(self,master,text, font, size, relx, rely, anchor):
    texto = ctk.CTkLabel(master, text=text, font=(font, size))
    texto.place(relx=relx, rely=rely, anchor=anchor)

  def botao(self, master, text, font, size, width, height, color, text_color, command,relx, rely, anchor):
    botao = ctk.CTkButton(master, text=text, width=width, height=height, font=(font, size), fg_color=color, text_color=text_color, command=command)
    botao.place(relx=relx, rely=rely, anchor=anchor)
    return botao
  
  def imagem(self, name, master, relx, rely, anchor, x, y):
    imagem = ctk.CTkImage(Image.open(f"{self.basePath()}/{name}"), size=(x, y))
    imagem_place = ctk.CTkLabel(master, image=imagem, text='')
    imagem_place.place(relx=relx, rely=rely, anchor=anchor)

  def Start_App(self):
    self.imagem("logo.png", self.root, 0.5, 0.15, "c", 140, 140)

    self.texto(self.root, "Balisong Flipping Tracker", "JetBrains Mono", 32, 0.5, 0.3, "c")

    self.botao(self.root, "Beginner", "JetBrains Mono", 18, 240, 40, "Green", "White", lambda: Begginer().Start_Begginer(), 0.3, 0.5, "c")
    self.botao(self.root, "Intermediate", "JetBrains Mono", 18, 240, 40, "Orange", "Black",None, 0.5, 0.5, "c")
    self.botao(self.root, "Advanced", "JetBrains Mono", 18, 240, 40, "Yellow", "Black",None, 0.7, 0.5, "c")

    self.root.mainloop()

if __name__ == "__main__":
  Main().Start_App()