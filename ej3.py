import tkinter as tk
from tkinter import ttk
import json

productos = []

umbral_bajo = 10
umbral_critico = 3

def limpiar(ent):
    ent.delete(0, tk.END)

def limpiar_todo():
    limpiar(id_prod)
    limpiar(nombre)
    limpiar(precio)
    limpiar(cant)
    limpiar(categoria)

def guardar_json():
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo, indent=4)

def cargar_json():
    global productos
    try:
        with open("productos.json", "r") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        productos = []

def guardar():
    id = id_prod.get()
    for prod in productos:
        if prod["id"] == id:
            campo_vacio.grid_remove()
            cantidad_int.grid_remove()
            id_existe.grid(row=7, column=0, columnspan=2, pady=10)
            limpiar_todo()
            return
    if id_prod.get() == "" or nombre.get() == "" or precio.get() == "" or cant.get() == "" or categoria.get() == "":
        id_existe.grid_remove()
        cantidad_int.grid_remove()
        campo_vacio.grid(row=7, column=0, columnspan=2, pady=10)
        limpiar_todo()
    else:
        try:
            int(cant.get())
        except ValueError:
            campo_vacio.grid_remove()
            id_existe.grid_remove()
            cantidad_int.grid(row=7, column=0, columnspan=2, pady=10)
        else:
            campo_vacio.grid_remove()
            id_existe.grid_remove()
            cantidad_int.grid_remove()
            productito = {"id":id, "nombre":nombre.get(), "precio":precio.get(), "cantidad":cant.get(), "categoria":categoria.get()}
            productos.append(productito)
            guardar_json()
            refrescar_tabla()
            limpiar_todo()

def leer_prod(event):
    selec = tree.selection()
    valores = tree.item(selec[0], "values")
    
    limpiar_todo()
    
    id_prod.insert(0, valores[0])
    nombre.insert(0, valores[1])
    precio.insert(0, valores[2])
    cant.insert(0, valores[3])
    categoria.insert(0, valores[4])

def modificar():
    try:
        int(cant.get())
    except ValueError:
        campo_vacio.grid_remove()
        id_existe.grid_remove()
        cantidad_int.grid(row=7, column=0, columnspan=2, pady=10)
    else:
        for i, prod in enumerate(productos):
            if id_prod.get() == prod["id"]:
                productos.pop(i)
                productito = {"id":id_prod.get(), "nombre":nombre.get(), "precio":precio.get(), "cantidad":cant.get(), "categoria":categoria.get()}
                productos.append(productito)
                limpiar_todo()
    guardar_json()
    refrescar_tabla()

def borrar():
    actual = {"id":id_prod.get(), "nombre":nombre.get(), "precio":precio.get(), "cantidad":cant.get(), "categoria":categoria.get()}
    for i, prod in enumerate(productos):
        if prod == actual:
            productos.pop(i)
    refrescar_tabla()
    guardar_json()
    limpiar_todo()

def refrescar_tabla():
    filtro = busqueda.get().lower()

    for fila in tree.get_children():
        tree.delete(fila)

    for prod in productos:
        if filtro in prod["nombre"].lower():
            
            cantidad = int(prod["cantidad"])
            tag = ""

            if cantidad <= umbral_critico:
                tag = "critico"
            elif cantidad <= umbral_bajo:
                tag = "bajo"

            tree.insert("", tk.END, values=(
                prod["id"],
                prod["nombre"],
                prod["precio"],
                prod["cantidad"],
                prod["categoria"]
            ), tags=(tag,))

root = tk.Tk()
root.title("Sistema de Gestión de Inventario")
root.geometry("800x450")
root.resizable(False, False)

hm1 = ttk.LabelFrame(root, text="Panel de Operaciones")
hm1.place(x=10, y=10, width=235, height=430)

hm2 = ttk.LabelFrame(root, text="Inventario")
hm2.place(x=255, y=10, width=535, height=430)

busqueda = tk.StringVar()
entry_busqueda = ttk.Entry(hm2, textvariable=busqueda)
entry_busqueda.pack(fill="x", padx=10, pady=5)
entry_busqueda.bind("<KeyRelease>", lambda e: refrescar_tabla())

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

#labels errores
id_existe = ttk.Label(hm1, text="Ya existe un producto con esa ID.", foreground="red")
campo_vacio = ttk.Label(hm1, text="No podes dejar ningún campo vacío.", foreground="red")
cantidad_int = ttk.Label(hm1, text="La cantidad debe ser un número.", foreground="red")

#treeview
tree = ttk.Treeview(hm2, columns=("ID", "Nombre", "Precio", "Cantidad", "Categoria"), show="headings")
tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Precio", text="Precio")
tree.heading("Cantidad", text="Cantidad")
tree.heading("Categoria", text="Categoria")
tree.column("ID", width=50)
tree.column("Nombre", width=100)
tree.column("Precio", width=70)
tree.column("Cantidad", width=70)
tree.column("Categoria", width=100)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

tree.bind("<ButtonRelease-1>", leer_prod)

tree.tag_configure("bajo", background="yellow")
tree.tag_configure("critico", background="red")

#cargar
cargar_json()
refrescar_tabla()

#loop
root.mainloop()