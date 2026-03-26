import tkinter as tk
from tkinter import ttk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 770
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100

root = tk.Tk()
root.title("Cancha")
root.geometry("600x770")
root.resizable(False, False)

imagenes = []
jugadores = []

cancha = tk.PhotoImage(file='assets/cancha.png')
imagenes.append(cancha)
cancha_l = tk.Label(root, image=cancha)
cancha_l.pack()

class Player:
    def __init__(self, root, image, x, y):
        self.root = root
        self.image = image
        
        self.label = tk.Label(root, image=image, bd=0)
        self.label.place(x=x, y=y)
        
        self.x = x
        self.y = y
        
        self.label.bind("<Button-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag)
        self.label.bind("<ButtonRelease-1>", self.drop)

        self.offset_x = 0
        self.offset_y = 0
    
    def start_drag(self, event):
        self.offset_x = event.x
        self.offset_y = event.y
        
        self.start_x = self.label.winfo_x()
        self.start_y = self.label.winfo_y()
    
    def drag(self, event):
        new_x = self.label.winfo_x() + event.x - self.offset_x
        new_y = self.label.winfo_y() + event.y - self.offset_y

        self.label.place(x=new_x, y=new_y)
    
    def drop(self, event):
        global jugadores

        my_x = self.label.winfo_x()
        my_y = self.label.winfo_y()
        
        cambio = False

        for other in jugadores:
            if other is self:
                continue

            ox = other.label.winfo_x()
            oy = other.label.winfo_y()

            if (abs(my_x - ox) < PLAYER_WIDTH // 2 and abs(my_y - oy) < PLAYER_HEIGHT // 2):
                self.label.place(x=ox, y=oy)
                other.label.place(x=self.start_x, y=self.start_y)
                
                cambio = True
                break
        if not cambio:
            self.label.place(x=self.start_x, y=self.start_y)

posiciones = [
    (250, 650),  # Arquero
    (50, 500), (183, 500), (316, 500), (450, 500), # Defensa
    (100, 350), (250, 350), (400, 350), # Medio
    (100, 150), (250, 100), (400, 150) # Ataque
]

for i in range(11):
    img = tk.PhotoImage(file=f"assets/jugador{i+1}.png")
    imagenes.append(img)

    x, y = posiciones[i]
    player = Player(root, img, x, y)
    jugadores.append(player)

root.mainloop()