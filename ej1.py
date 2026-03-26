import tkinter as tk
from tkinter import ttk
import math

#_____________ funciones _____________

def limpiar():
    entrada.delete(0, tk.END)

def calcular():#
    try:
        cosita = entrada.get()
        for char in cosita:
            if char not in "0123456789+-*/(). ":
                raise ValueError("Entrada inválida")
        resultado = eval(cosita)
        limpiar()
        if resultado.is_integer():
            entrada.insert(0, str(int(resultado)))
        else:
            entrada.insert(0, str(resultado))
    except:
        limpiar()

def potencia():
    try:
        cosita = entrada.get()
        for char in cosita:
            if char not in "-.0123456789 ":
                raise ValueError("Entrada inválida")
        resultado = float(cosita) * float(cosita)
        limpiar()
        if resultado.is_integer():
            entrada.insert(0, str(int(resultado)))
        else:
            entrada.insert(0, str(resultado))
    except:
        limpiar()

def raiz():
    try:
        cosita = entrada.get()
        for char in cosita:
            if char not in ".0123456789 " or float(cosita) < 0:
                raise ValueError("Entrada inválida")
        resultado = math.sqrt(float(cosita))
        limpiar()
        if resultado.is_integer():
            entrada.insert(0, str(int(resultado)))
        else:
            entrada.insert(0, str(resultado))
    except:
        limpiar()

#_____________ root y mas cositas no se _____________

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x150")
root.configure(bg="#f5bad4")
root.resizable(False, False)

entrada = ttk.Entry(root, font=("Trebuchet MS", 15))
entrada.pack(fill="x", padx=20, pady=20)

frame = ttk.Frame(root)
frame.pack()

#_____________ botoncitos _____________

igual = ttk.Button(frame, text="=", command=calcular)
igual.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10)
potenciar = ttk.Button(frame, text="x²", command=potencia).grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=10)

raizear = ttk.Button(frame, text="√", command=raiz).grid(row=0, column=2, padx=5, pady=5, ipadx=10, ipady=10)

#_____________ main loop _____________

root.mainloop()