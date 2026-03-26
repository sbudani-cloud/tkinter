import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sistema de Gestión de Inventario")
root.geometry("400x450")
root.resizable(False, False)

hm1 = ttk.LabelFrame(root, text="Panel de Operaciones")
hm1.place(x=10, y=10, width=185, height=430)

hm2 = ttk.LabelFrame(root, text="LOL")
hm2.place(x=205, y=10, width=185, height=430)

root.mainloop()