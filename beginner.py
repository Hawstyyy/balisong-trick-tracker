import customtkinter as ctk
from PIL import Image
import os, sys
import webbrowser
import json

class Begginer:
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.geometry("1280x720")
    self.root.resizable(False, False)
    self.root.title("Balisong Flipping Tracker")
    self.root.iconbitmap(f"{self.basePath()}/logo.ico")
    with open("checks.json") as file:
      self.state = json.load(file)

  def teste(self):
    url = "https://www.google.com/search?q=Balisong"
    webbrowser.open(url, new=0, autoraise=True)

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
  
  def checkbox(self, master, text, font, size, variable, relx, rely, anchor):
    checkbox = ctk.CTkCheckBox(master, text=text, font=(font, size), variable=self.state.get(variable))
    checkbox.place(relx=relx, rely=rely, anchor=anchor)
    return checkbox
  def checkCheckbox(self, checkbox, id):
    state = checkbox.get()
    with open("checks.json", "w") as file:
      json.dump(f"{id}: {state}", file)
  def Start_Begginer(self):
    self.botao(self.root, "teste", "JetBrains Mono",20 ,240, 40, "Dark Blue", "White", self.teste, 0.5, 0.5, "c")

    checkbox = self.checkbox(self.root, "Aprendido", "JetBrains Mono", 16, "aprendido", 0.2, 0.5, "c")
    checkbox.configure(command=lambda: self.checkCheckbox(checkbox, "aprendido"))

    self.root.mainloop()

if __name__ == "__main__":
  Begginer().Start_Begginer()