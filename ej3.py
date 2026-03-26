import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sistema de Gestión de Inventario")
root.geometry("500x450")
root.resizable(False, False)

hm1 = ttk.LabelFrame(root, text="Panel de Operaciones")
hm1.place(x=10, y=10, width=235, height=430)

hm2 = ttk.LabelFrame(root, text="Inventario")
hm2.place(x=255, y=10, width=235, height=430)

#_________los entrys del hemisferio unito
id_prod_label = ttk.Label(hm1, text="ID Producto").grid(row=0, column=0, padx=5, pady=5)
id_prod = ttk.Entry(hm1).grid(row=0, column=1, padx=5, pady=5)

nombre_label = ttk.Label(hm1, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
nombre = ttk.Entry(hm1).grid(row=1, column=1, padx=5, pady=5)

precio_label = ttk.Label(hm1, text="Precio").grid(row=2, column=0, padx=5, pady=5)
precio = ttk.Entry(hm1).grid(row=2, column=1, padx=5, pady=5)

cant_label = ttk.Label(hm1, text="Cantidad").grid(row=3, column=0, padx=5, pady=5)
cant = ttk.Entry(hm1).grid(row=3, column=1, padx=5, pady=5)

categoria_label = ttk.Label(hm1, text="Categoria").grid(row=4, column=0, padx=5, pady=5)
categoria = ttk.Entry(hm1).grid(row=4, column=1, padx=5, pady=5)

#btonocitos
guardar = ttk.Button(hm1, text="Guardar").grid(row=5, column=0, padx=5, pady=5)
modificar = ttk.Button(hm1, text="Modificar").grid(row=5, column=1, padx=5, pady=5)
borrar = ttk.Button(hm1, text="Borrar").grid(row=6, column=0, padx=5, pady=5)

#loop
root.mainloop()