import tkinter as tk
from tkinter import ttk

productos = []

def limpiar(ent):
    ent.delete(0, tk.END)

def guardar():
    id = id_prod.get()
    for prod in productos:
        if prod["id"] == id:
            print("Ya existe un producto con esa id.")
            break
    if id_prod.get() == "" or nombre.get() == "" or precio.get() == "" or cant.get() == "" or categoria.get() == "":
        print("No podes dejar ningún campo vacío.")
    else: #falta guardarlo en un json
        productito = {"id":id, "nombre":nombre.get(), "precio":precio.get(), "cantidad":cant.get(), "categoria":categoria.get()}
        productos.append(productito)
        limpiar(id_prod)
        limpiar(nombre)
        limpiar(precio)
        limpiar(cant)
        limpiar(categoria)
        print(productos)

def modificar():
    pass

def borrar():
    pass

def refrescar_tabla():
    for fila in tree.get_children():
        tree.delete(fila)

    for prod in productos:
        tree.insert("", tk.END, values=(
            prod["id"],
            prod["nombre"],
            prod["precio"],
            prod["cantidad"],
            prod["categoria"]
        ))

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
id_prod = ttk.Entry(hm1)
id_prod.grid(row=0, column=1, padx=5, pady=5)

nombre_label = ttk.Label(hm1, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
nombre = ttk.Entry(hm1)
nombre.grid(row=1, column=1, padx=5, pady=5)

precio_label = ttk.Label(hm1, text="Precio").grid(row=2, column=0, padx=5, pady=5)
precio = ttk.Entry(hm1)
precio.grid(row=2, column=1, padx=5, pady=5)

cant_label = ttk.Label(hm1, text="Cantidad").grid(row=3, column=0, padx=5, pady=5)
cant = ttk.Entry(hm1)
cant.grid(row=3, column=1, padx=5, pady=5)

categoria_label = ttk.Label(hm1, text="Categoria").grid(row=4, column=0, padx=5, pady=5)
categoria = ttk.Entry(hm1)
categoria.grid(row=4, column=1, padx=5, pady=5)

#btonocitos
bguardar = ttk.Button(hm1, text="Guardar", command=guardar).grid(row=5, column=0, padx=5, pady=5)
bmodificar = ttk.Button(hm1, text="Modificar", command=modificar).grid(row=5, column=1, padx=5, pady=5)
bborrar = ttk.Button(hm1, text="Borrar", command=borrar).grid(row=6, column=0, padx=5, pady=5)

#treeview
tree = ttk.Treeview(hm2)
tree.pack(fill="both", expand=True, padx=10, pady=10)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

#loop
root.mainloop()