import tkinter as tk
from tkinter import ttk
from utilites import *
from algorithmes import *
from affichage import *

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.titre = tk.Label(self, text="Labyrinthes", borderwidth=23, font="Comic 18")
        self.titre.pack()
        self.combo = ttk.Combobox(self, values=["Pseudolabyrinthe", "Labyrinthe"])
        self.combo.pack()
        self.j=""
        self.entry = tk.Entry(self, width=20,textvariable=self.j)
        self.entry.pack()
        self.button = tk.Button(self, command=self.action_button, fg="blue", text="Créer")
        self.button.pack()

        self.button.bind(self.turn_red)
    
    def turn_red(self, event):
        event.widget["activeforeground"] = "red"

    def action_button(self):
        import pickle
        option = self.combo.get()
        taille = self.entry.get()
        taille = taille.split(",")
        M = int(taille[0])
        N = int(taille[1])
        if option == "Pseudolabyrinthe":
            import random
            resultat = random.choice(get_PseudoLabyrinthes((M,N)))
        if option == "Labyrinthe":
            import random
            resultat = random.choice(get_Labyrinthes((M,N)))
        print(resultat)
        with open("pick","wb") as f:
            pickle.dump(resultat, f)


root = tk.Tk()
app = App(root)
app.mainloop()
