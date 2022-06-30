import tkinter as tk

window = tk.Tk()

ListaElementos = tk.Listbox(window)

for i in ["Opcion1", "Opcion2", "Opcion3", "Opcion4", "Opcion5"]:
    ListaElementos.insert(tk.END, i)

ListaElementos.pack()

label = tk.Label(text="Seleccione su opcion")
label.pack()

window.mainloop()