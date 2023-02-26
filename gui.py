import tkinter as tk
from tkinter import ttk
from utilites import *
from algorithmes import *

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.titre = tk.Label(self, text="Labyrinthes", borderwidth=23)
        self.titre.pack()

        self.button = tk.Button(self, command=self.c, bg="yellow", fg="blue", text="Button")
        self.button.pack()
        self.button.bind("<Enter>", self.turn_red)
        self.entry = tk.Entry(self, width=20)
        self.entry.pack()
        self.combo = ttk.Combobox(self, values=["Pseudolabyrinthe", "Labyrinthe"])
        self.combo.pack()
    
    def turn_red(self, event):
        event.widget["activeforeground"] = "red"

    def c(self):
        print("e")

root = tk.Tk()
app = App(root)
app.mainloop()
